# Agrin's Object Tracking with YOLOv8

## Overview

This project demonstrates real-time object detection and tracking using the YOLOv8 model. The code captures video input from a camera, processes each frame to detect objects, and then draws bounding boxes and labels around detected objects in real-time.

## Features

- Real-time object detection using YOLOv8.
- Bounding box and label display for detected objects.
- Customizable input source (webcam by default).
- Simple and efficient implementation using OpenCV and the Ultralytics YOLO package.

## Getting Started

Follow these steps to get the project up and running:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Agrinsadon/ObjectDetection.git
    cd ObjectDetection
    ```

2. **Install the required dependencies:**

    ```bash
    pip install ultralytics
    ```

3. **Run the script:**

    ```bash
    python main.py
    ```

5. **Interact with the application:**

    - The application will open a window displaying the video feed with detected objects highlighted by bounding boxes.
    - Press the `ESC` key to exit the application.

## Customization

- **Model:** The code uses the YOLOv8 medium model (`yolov8m.pt`). You can change the model to other versions by replacing the file name (e.g., `yolov8n.pt` for the nano model).

- **Bounding Box Color:** The bounding box color is set to `(10, 10, 10)` (dark gray). You can change this color by modifying the `cv2.rectangle` function call.

- **Text Settings:** The label font and size are customizable. You can change the font type, size, color, and thickness in the `cv2.putText` function call.

