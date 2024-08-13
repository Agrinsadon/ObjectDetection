import cv2
from ultralytics import YOLO
import numpy as np

# if not working try to switch it to 1
cap = cv2.VideoCapture(0)

model = YOLO("yolov8m.pt")

class_names = model.names

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    results = model(frame)

    for result in results:
        bboxes = np.array(result.boxes.xyxy, dtype="int")
        classes = np.array(result.boxes.cls, dtype="int")

        for cls, bbox in zip(classes, bboxes):
            (x, y, x2, y2) = bbox

            cv2.rectangle(frame, (x, y), (x2, y2), (10, 10, 10), 2)

            label = class_names[cls]
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Agrin's Object Tracking", frame)

    # Break loop pressing "ESC"
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
