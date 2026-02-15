import cv2
import os

from os.path import exists

try:
    img_count=0
    dataset_dir = os.getcwd()+"\\dataset\\"
    person_dir = str(input("Person Name: "))
    person_dir = dataset_dir+person_dir

    max_img_count = int(input("Max img count: "))

    if not exists(dataset_dir):
        os.mkdir(dataset_dir)
    if not exists(person_dir):
        os.mkdir(person_dir)

    _cam = cv2.VideoCapture(0)  # Webcam
    while _cam.isOpened():
        _stat, _frame = _cam.read()
        if not _stat:break
        _frame=cv2.flip(_frame,1)

        cv2.imshow("Preview",_frame)

        img_name=person_dir+"\\img_{}.jpg".format(img_count+1)
        img_count+=1
        print(f"Taking Photo... {img_name}")
        cv2.imwrite(img_name,_frame)
        if img_count>=max_img_count:break
        
        if cv2.waitKey(5)&0xFF==27 or img_count==max_img_count:break

    _cam.release()
    cv2.destroyAllWindows()
except Exception as err:
    print(err)
