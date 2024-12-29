import cv2 
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe.python.solutions.drawing_styles as styles

hands=mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5    
)

cap=cv2.VideoCapture(0) #show your pc cam or show your 'video.mp4'
while cap.isOpened():
    status,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hands_detect=hands.process(frame)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    if hands_detect.multi_hand_landmarks:
        for hand_landmark in hands_detect.multi_hand_landmarks:
            
            drawing_spec_landmarks = styles.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2)
            drawing_spec_connections = styles.DrawingSpec(color=(255, 0, 255), thickness=2) 
            
            drawing.draw_landmarks(
                frame,hand_landmark,
                mp_hands.HAND_CONNECTIONS,
                drawing_spec_landmarks, #or drawing_styles.get_default_hand_landmarks_style()
                drawing_spec_connections, #or drawing_styles.get_default_hand_connections_style()

            )
    cv2.imshow("El Yakalama",frame)
    if cv2.waitKey(5) & 0xFF==27:break #Press to 'ESC' for exit 

cv2.destroyAllWindows()
cap.release()