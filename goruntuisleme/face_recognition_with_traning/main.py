import cv2
import cv2.data
import time
import os
from os.path import exists
import json

try:
    with open("labels.json", "r") as f:
        label_map = json.load(f)
except:
    print("Error: labels.json not found! Run the trainer.py file first.")
    exit()
yuz = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

cam = cv2.VideoCapture(0)

prev_time = 0
img_count = 0
while cam.isOpened():
	stat, frame = cam.read()
	if not stat: break
	frame = cv2.flip(frame, 1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	yuzler = yuz.detectMultiScale(gray, 1.3)
	now_time = time.time()
	fps = int(1/(now_time-prev_time))
	prev_time = now_time
	cv2.putText(frame, "FPS:"+str(fps), (5, 25),
	            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 1)

	for (x, y, w, h) in yuzler:
			id_str, conf = recognizer.predict(gray[y:y+h, x:x+w])
			if conf < 75: 
				name = label_map.get(str(id_str), "UNKNOWN")
				color = (0, 255, 0)
			else:
				name = "UNKNOWN"
				color = (0, 0, 255)

			cv2.putText(frame, f"{name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)
			cv2.rectangle(frame, (x, y), (x+w, y+h), color, 1)    
		
	cv2.imshow("Preview", frame)
	if cv2.waitKey(1) & 0xFF == 27: break
	
cv2.destroyAllWindows()
cam.release()
