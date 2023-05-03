import cv2
from ultralytics import YOLO
import supervision as sv
import easyocr
import tkinter as tk
from PIL import Image, ImageTk
import connect

# reader = easyocr.Reader(['en'])
# cap = cv2.VideoCapture(0)
# model = YOLO('best.pt')
def add_detail(frame, detections):
    box_annotate = sv.BoxAnnotator(
        thickness = 1,
        text_thickness = 1,
        text_scale = 1
    )
    labels = [
        f"{model.model.names[class_id]} {confidence: 0.2f}"
        for _, confidence, class_id, _
        in detections
    ]
    frame = box_annotate.annotate(
        scene=frame,
        detections=detections,
        labels=labels
    )
# # details
# box_annotate = sv.BoxAnnotator(
#     thickness = 1,
#     text_thickness = 1,
#     text_scale = 1
# )

# # main code
# while True:
#     ret, frame = cap.read()
#     result = model(frame)[0]
#     detections = sv.Detections.from_yolov8(result)

#     # create a box around the plate
#     # labels = [
#     #     f"{model.model.names[class_id]} {confidence: 0.2f}"
#     #     for _, confidence, class_id, _
#     #     in detections
#     # ]
#     # frame = box_annotate.annotate(
#     #     scene=frame,
#     #     detections=detections,
#     #     labels=labels
#     # )

#     # ROI
#     key = cv2.waitKey(1)
#     if(detections):
#         roi = detections.xyxy[0]
#         x1 = int(roi[0])
#         y1 = int(roi[1])
#         x2 = int(roi[2])
#         y2 = int(roi[3])
        
#         plate = frame[y1:y2, x1:x2]
#         result = reader.readtext(plate, detail=0, paragraph=True)
#         print(result)

#     cv2.imshow('result', frame)
    
#     if cv2.waitKey(1) & 0xFF == 27: # 27 = esc button
#         break

# cap.release()
# cv2.destroyAllWindows()

model = YOLO('best.pt')
reader = easyocr.Reader(['en'])

def detection_result(frame, yolov8_result):
    detections = sv.Detections.from_yolov8(yolov8_result)
    add_detail(frame, detections)
    
    if (detections):
        roi = detections.xyxy[0]
        x1 = int(roi[0])
        y1 = int(roi[1])
        x2 = int(roi[2])
        y2 = int(roi[3])
        
        plate = frame[y1:y2, x1:x2]
        plate_print = reader.readtext(plate, detail=0, paragraph=True)
        return plate_print

def camera_init(cap):
    ret, frame = cap.read()
    result = model(frame)[0]
    return result

def show_camera_tkinter(frame, video_label):
    # Convert the frame to a tkinter compatible format
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)

    # Update the label with the new frame
    video_label.imgtk = img
    video_label.configure(image=img)

# cap = cv2.videoCapture(0)
# camera_init(cap)
# plate = detection_result(cap)