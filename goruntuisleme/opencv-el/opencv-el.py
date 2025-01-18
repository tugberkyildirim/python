import cv2
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe.python.solutions.drawing_styles as styles

hand_type=""
hands=mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5    
)
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    frame = cv2.flip(frame, 1)
    if status:
        print("Baglanti Basarili")
    elif not status:
        print("Baglanti Basarisiz")
        break
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    res=hands.process(frame)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.putText(frame,"Cikmak Icin 'ESC' Tusuna Basiniz.",(5,25),cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,0,255),1,cv2.LINE_AA)
    if res.multi_hand_landmarks:
        hand_count=len(res.multi_hand_landmarks)
        cv2.putText(frame,"El Sayisi: "+str(hand_count),(5,55),cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,0,255),1,cv2.LINE_AA)
        for hand_landmarks in res.multi_hand_landmarks:
            for landmarks in hand_landmarks.landmark:
                h,w,_=frame.shape
                x,y=int(landmarks.x*w),int(landmarks.y*h)
                
                drawing_spec_landmarks = styles.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=2)
                drawing_spec_connections = styles.DrawingSpec(color=(0, 0, 255), thickness=2) 
                
                drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    drawing_spec_landmarks,
                    drawing_spec_connections
                )
                wrist=hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                thumb=hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                hand_type = "Sol El" if res.multi_handedness[0].classification[0].label == 'Left' else "Sag El"
                if hand_count>1:hand_type="Birden Fazla El"
                cv2.putText(frame,hand_type,(5,85),cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,0,0),1,cv2.LINE_AA)
                h,w,_=frame.shape
    cv2.imshow("El Tespit",frame)
    if cv2.waitKey(5)& 0xFF==27:
        break
                