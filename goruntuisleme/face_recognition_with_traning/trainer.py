import cv2
import numpy as np
import os
import json 

dataset_path = "dataset"
faces = []
labels = []
label_map = {}
current_label = 0

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


for person_name in sorted(os.listdir(dataset_path)):
    person_path = os.path.join(dataset_path, person_name)
    if not os.path.isdir(person_path): continue

    label_map[current_label] = person_name 

    for image_name in os.listdir(person_path):
        img_path = os.path.join(person_path, image_name)
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detected_faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in detected_faces:
            faces.append(gray[y:y+h, x:x+w])
            labels.append(current_label)

    current_label += 1

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))
recognizer.save("trainer.yml")

with open("labels.json", "w") as f:
    json.dump(label_map, f)

print(f"Traning complete. {len(label_map)} person registered.")