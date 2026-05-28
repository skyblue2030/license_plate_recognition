import cv2
import time
import os
from ultralytics import YOLO

# Tạo thư mục lưu ảnh crop và ảnh đã nhận diện
os.makedirs("output/plates", exist_ok=True)
os.makedirs("output/annotated", exist_ok=True)
bbox_log_path = "output/bounding_boxes.txt"

# Load models
yolo_LP_detect = YOLO("detect_weight/weights/best.pt")
yolo_license_plate = YOLO("reg_weight/weights/best.pt")
yolo_LP_detect.conf = 0.5
yolo_license_plate.conf = 0.30

prev_frame_time = 0
vid = cv2.VideoCapture(0)

frame_index = 0  # Đánh số ảnh lưu

while True:
    ret, frame = vid.read()
    if not ret:
        break

    results = yolo_LP_detect(frame)[0]
    list_read_plates = set()

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        label = f"license plate {conf:.2f}"

        # Vẽ bounding box và nhãn confidence
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Crop vùng biển số
        crop_img = frame[y1:y2, x1:x2]

        # Lưu ảnh crop
        timestamp = int(time.time() * 1000)
        crop_filename = f"output/plates/plate_{timestamp}.jpg"
        cv2.imwrite(crop_filename, crop_img)

        # Ghi bounding box vào log
        with open(bbox_log_path, "a") as f:
            f.write(f"{crop_filename},{x1},{y1},{x2},{y2}\n")

        # OCR biển số
        ocr_result = yolo_license_plate(crop_img)[0]
        plate_text = ""
        if ocr_result and len(ocr_result.boxes) > 0:
            chars = []
            for b in ocr_result.boxes:
                x_min, y_min, x_max, y_max = b.xyxy[0]
                x_center = (x_min + x_max) / 2
                y_center = (y_min + y_max) / 2
                cls = int(b.cls[0])
                char = ocr_result.names[cls] if hasattr(ocr_result, 'names') else str(cls)
                chars.append((x_center, y_center, char))

            if len(chars) > 1:
                y_values = [c[1] for c in chars]
                y_mean = sum(y_values) / len(y_values)
                top_line = [c for c in chars if c[1] < y_mean]
                bottom_line = [c for c in chars if c[1] >= y_mean]

                top_line.sort(key=lambda c: c[0])
                bottom_line.sort(key=lambda c: c[0])

                plate_text = ''.join([c[2] for c in top_line]) + '\n' + ''.join([c[2] for c in bottom_line])
            else:
                plate_text = chars[0][2]

            list_read_plates.add(plate_text)

            # Hiển thị biển số 2 dòng màu xanh lá cây
            for i, line in enumerate(plate_text.split('\n')):
                cv2.putText(frame, line, (x1, y2 + 30 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)

    # Tính FPS
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time) if prev_frame_time > 0 else 0
    prev_frame_time = new_frame_time
    cv2.putText(frame, f'FPS: {int(fps)}', (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 255, 0), 3)

    # Lưu ảnh annotated
    annotated_path = f"output/annotated/frame_{frame_index}.jpg"
    cv2.imwrite(annotated_path, frame)
    frame_index += 1

    cv2.imshow('License Plate Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
