import cv2
from ultralytics import YOLO

cv2.namedWindow("Office Detector", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Office Detector",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
camera=cv2.VideoCapture(0)
#model=YOLO("yolov8n.pt")
model=YOLO("yolov8n-seg.pt")
while camera.isOpened():
    status,frame=camera.read()
    if not status:break
    frame=cv2.flip(frame,1)
    results=model.track(frame,classes=[0,41,56,62,63,64,66,39],conf=0.5,imgsz=640,persist=True)
    cv2.imshow("Office Detector",results[0].plot())
    if cv2.waitKey(5)&0xFF==27:break

camera.release()
cv2.destroyAllWindows()
