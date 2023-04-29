import cv2
from ultralytics import YOLO
import supervision as sv
import easyocr

reader = easyocr.Reader(['en'])
cap = cv2.VideoCapture(0)
model = YOLO('best.pt')

# details
box_annotate = sv.BoxAnnotator(
    thickness = 1,
    text_thickness = 1,
    text_scale = 1
)

# main code
while True:
    ret, frame = cap.read()
    result = model(frame)[0]
    detections = sv.Detections.from_yolov8(result)

    # create a box around the plate
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

    # ROI
    key = cv2.waitKey(1)
    if(detections):
        roi = detections.xyxy[0]
        x1 = int(roi[0])
        y1 = int(roi[1])
        x2 = int(roi[2])
        y2 = int(roi[3])
        
        plate = frame[y1:y2, x1:x2]
        result = reader.readtext(plate, detail=0, paragraph=True)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print(result)
            print('bo may la xe 1')
        if cv2.waitKey(1) & 0xFF == ord('w'):
            print(result)
            print('tao la xe so 2')
        
    # camera screen
    cv2.imshow('result', frame)
    
    if cv2.waitKey(1) & 0xFF == 27: # 27 = esc button
        break

cap.release()
cv2.destroyAllWindows()