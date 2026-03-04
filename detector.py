from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

model = YOLO("yolov8n.pt") 

def detect_objects(image_bytes: bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    results = model(img)

    annotated_frame = results[0].plot()

    _, buffer = cv2.imencode(".jpg", annotated_frame)
    return buffer.tobytes()