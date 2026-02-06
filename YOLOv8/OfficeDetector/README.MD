# 🏢 Office Detector (YOLOv8 + OpenCV)

This project uses **YOLOv8** and **OpenCV** to detect and track objects commonly found in office environments in real-time camera footage.  
Thanks to the segmentation model, objects are displayed not only with boxes but also with their **masks**.

## 🚀 Features

- Real-time object detection
- YOLOv8 **segmentation** model (`yolov8n-seg`)
- Object **tracking**
- Full-screen camera view
- Filtering for specific classes
- Webcam support

## 🧠 Detected Classes

The model only detects the following COCO classes:

- 👤 Person
- 💻 Laptop
- ⌨️ Keyboard
- 🖱️ Mouse
- 📱 Cell Phone
- 📚 Book
- 🪑 Chair
- 🖥️ TV / Monitor

(Classes can be customized with the `classes` parameter.)

## 📦 Requirements

- Python 3.8+
- OpenCV
- Ultralytics YOLOv8

## 🔧 Installation

```bash
pip install opencv-python ultralytics
```