# OpenCV LBPH Face Recognition System
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
<br/>
This project provides a real-time face recognition system using the OpenCV library and the LBPH (Local Binary Patterns Histograms) algorithm. The system consists of three main stages: data collection, model training, and real-time recognition.

### 🚀 Features
**Data Collection:** Automatic photo capture and organized naming via webcam.

**Model Training:** Training the LBPH face recognition model with the collected dataset.

**Real-Time Recognition:** Real-time identity detection from camera feed using the trained model.

**Optimized Detection:** Face detection powered by Haar Cascade classifiers.

### 📋 Requirements
To ensure the project runs smoothly, the following library versions are recommended:

```
opencv-contrib-python==4.8.1.78
numpy==1.26.4
```
Note: Use opencv-contrib-python instead of the standard opencv-python, as it contains the necessary face module for recognition algorithms.


### 📖 Usage Instructions
Follow these steps in order to operate the system:

* 1. Data Collection (take_photo.py)
Run this to capture photos of the person you want the system to recognize.
It will prompt for a **"Person Name"** and **"Max img count"**.
Photos are automatically saved under the `dataset/` directory in a folder named after the person.

* 2. Model Training (trainer.py)
Processes the images in the dataset/ folder to train the model.
Once completed, it generates a trainer.yml file (containing face data) and a labels.json file (mapping IDs to names).

* 3. Face Recognition (main.py)
Run this to start the live recognition system.

The camera will open, detect faces, and display the name and confidence level of recognized individuals on the screen.

### 📂 File Structure
**main.py:** Main script for real-time recognition.
**take_photo.py:** Tool for creating the dataset.
**trainer.py:** Script for training the LBPH algorithm.
**haarcascade_frontalface_default.xml:** Pre-trained OpenCV model for face detection.
dataset/: (Auto-generated) Folder where training photos are stored.

### ⚠️ Important Notes
Collecting data in a well-lit environment significantly improves recognition accuracy.


You must run `trainer.py` at least once before starting `main.py.`


