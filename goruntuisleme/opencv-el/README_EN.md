# Hand Detection Application (OpenCV and Mediapipe)

This project uses OpenCV and Mediapipe libraries to perform real-time hand detection and tracking. The application detects hands in frames captured via a webcam, draws finger joints, and displays the number of detected hands on the screen.

## Features

- **Hand Detection:** Detection of up to two hands.
- **Finger Skeleton Drawing:** Draws the finger joints and connections of detected hands.
- **Hand Type Detection:** Identifies whether the detected hand is the left or right hand.
- **User Guidance:** Displays a message indicating that the "ESC" key can be pressed to exit the application.

## Requirements

To run this application, the following libraries must be installed:

- Python 3.7 or higher
- OpenCV
- Mediapipe

You can install the required libraries using the following command:

```bash
pip install opencv-python mediapipe
```

## Code Explanation

### Key Modules

- **cv2:** OpenCV library used for image processing and camera control.
- **mediapipe:** A powerful solution for hand detection and finger skeleton drawing.

### Main Workflow

1. **Hand Detection:**
   - Mediapipe's `Hands` module detects hands and finger joints.
   - The frame is converted to `RGB` format, and the hand detection process is performed.

2. **Finger Joint Drawing:**
   - Mediapipe's drawing functions are used to draw the finger joints of the detected hands.

3. **Hand Type Identification:**
   - Determines whether the detected hand is a left or right hand and displays it on the screen.

4. **Guidance and Exit:**
   - The application can be exited by pressing the "ESC" key while running.

### Running the Application

1. Run the code to start the camera:

   ```bash
   python opencv-el.py
   ```

2. Once the camera is active, you will see the detected hands and their finger joints.
3. Press the `ESC` key to exit the application.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.

---
