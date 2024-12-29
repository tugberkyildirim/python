import os,sys,cv2,cv2.data

yuz_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)#show your pc cam or show your 'video.mp4'

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuz=yuz_cascade.detectMultiScale(gray,1.3)
    yuzler=len(yuz)
    cv2.putText(frame,"Cikis Yapmak Icin 'ESC' Tusuna Basiniz",(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.45,(255,0,255))
    cv2.putText(frame,"Yuz Sayisi:"+str(yuzler),(10,55),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255))
    for (x,y,w,h)in yuz:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),1)
    
    cv2.imshow("Yuz Tanima",frame)
    if cv2.waitKey(5)& 0xFF==27:break  #Press to 'ESC' for exit 
cap.release()
cv2.destroyAllWindows()
    
