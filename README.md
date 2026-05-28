# Realtime License Plate Detection and Recognition using YOLOv8

## Overview

This project implements a realtime license plate detection and recognition system using YOLOv8 and Python.

The system performs:

* License plate detection
* Character recognition
* Realtime webcam inference
* Bounding box visualization
* Automatic plate text reconstruction

The project uses a two-stage YOLOv8 pipeline:

1. Detect license plate region
2. Detect and recognize characters inside the plate

---

# Features

* Realtime webcam processing
* Two-stage YOLOv8 inference pipeline
* Vietnamese license plate recognition
* Character sorting for multi-line license plates
* Bounding box logging
* FPS monitoring
* Annotated image saving

---

# Project Pipeline

Input Frame
→ License Plate Detection (YOLOv8)
→ Crop Plate Region
→ Character Detection (YOLOv8)
→ Character Sorting by Coordinates
→ Plate Text Reconstruction
→ Realtime Visualization

---

# Tech Stack

* Python
* OpenCV
* Ultralytics YOLOv8
* PyTorch
* NumPy

---

# Project Structure

```text
license-plate-recognition-yolov8/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── detect_weight/
├── reg_weight/
│
└──── output/
    ├── plates/
    └── annotated/

```

---

# Model Information

## License Plate Detection

* Model: YOLOv8n
* Number of classes: 1
* Class name: license plate

## Character Recognition

* Model: YOLOv8n
* Number of classes: 36
* Classes:

  * Digits: 0-9
  * Characters: A-Z

---

# Dataset Preparation

The dataset was divided into:

* Train set: 80%
* Validation set: 20%

YAML configuration files were used to define:

* Dataset paths
* Class names
* Number of classes

---

# Training Configuration

* Pretrained model: YOLOv8n.pt
* Image size: 640 × 640
* Epochs: 20
* Transfer learning applied

---

# Key Implementation Details

## Realtime Webcam Inference

The system captures video frames from webcam and performs realtime detection and recognition.

## Character Sorting Logic

Detected characters are sorted based on:

* X-axis position
* Y-axis position

This allows the system to correctly reconstruct:

* Single-line plates
* Multi-line plates

## Bounding Box Logging

Detected plate coordinates are automatically stored for later analysis.

## FPS Monitoring

Realtime FPS calculation is implemented to evaluate inference performance.

---

# Results

## Detection Performance

* Accuracy: ~95%
* F1-score: ~92%

## System Capabilities

* Detects multiple license plates
* Supports realtime processing
* Handles multi-line plates
* Saves annotated outputs automatically

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/license-plate-recognition-yolov8.git
cd license-plate-recognition-yolov8
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python main.py
```

Press:

```text
q
```

to exit the application.

---

# Output

The system automatically saves:

* Cropped license plate images
* Annotated detection frames
* Bounding box logs

Output folders:

```text
output/plates/
output/annotated/
```

---

# Future Improvements

* Improve OCR accuracy in low-light environments
* Add video file inference support
* Deploy as Flask API
* Optimize inference speed
* Add automatic plate tracking

---

# Demo

## Detection Result



## Realtime Inference



---

# Learning Outcomes

Through this project, I gained practical experience in:

* Computer vision pipelines
* YOLOv8 training and inference
* Dataset preprocessing
* Realtime video processing
* Model evaluation using F1-score and confusion matrix
* Python-based AI application development

---

# Author

Tran Van Si
Posts and Telecommunications Institute of Technology (PTIT)
