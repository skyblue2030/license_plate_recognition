# 📌 Automatic License Plate Recognition (ALPR)

## 🚀 Giới thiệu
Hệ thống **Nhận diện biển số xe** (Automatic License Plate Recognition - ALPR) sử dụng OpenCV và Tesseract OCR để phát hiện và nhận diện biển số từ hình ảnh. Dự án này giúp nhận diện các ký tự trên biển số xe một cách tự động.

## 📷 Mô tả quy trình
Hệ thống hoạt động qua các bước:
1. **Tiền xử lý ảnh**: Chuyển đổi ảnh về grayscale, tăng độ tương phản, lọc nhiễu.
2. **Phát hiện biển số**: Sử dụng mô hình Haar Cascade để xác định vùng biển số.
3. **Trích xuất và xử lý biển số**: Cắt vùng biển số, chuẩn hóa kích thước và áp dụng ngưỡng (thresholding).
4. **Nhận diện ký tự**: Sử dụng Tesseract OCR để chuyển ảnh thành văn bản.
5. **Xuất kết quả**: Hiển thị biển số nhận diện được và vẽ vùng phát hiện trên ảnh gốc.

## 🛠️ Yêu cầu hệ thống
- Python 3.x
- OpenCV
- Tesseract OCR
- NumPy

## 📦 Cài đặt
Trước khi chạy chương trình, cài đặt các thư viện cần thiết:
```bash
pip install opencv-python pytesseract numpy
```

Ngoài ra, tải và cài đặt **Tesseract OCR**:
- Windows: [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- Linux/macOS: Cài đặt bằng trình quản lý gói, ví dụ: `sudo apt install tesseract-ocr`

## 🎯 Cách sử dụng
1. Đặt ảnh xe có biển số trong thư mục dự án.
2. Chỉnh sửa đường dẫn ảnh trong file `detect_license_plate.py`.
3. Chạy chương trình:
   ```bash
   python detect_license_plate.py
   ```
4. Kết quả sẽ hiển thị vùng biển số được phát hiện và văn bản nhận diện.

## 📌 Cải tiến tiềm năng
- Sử dụng Deep Learning (YOLO, CRNN) thay vì Haar Cascade.
- Hỗ trợ video và camera trực tiếp.
- Kết hợp với hệ thống quản lý phương tiện.

## 📜 Giấy phép
Tran Van Si

