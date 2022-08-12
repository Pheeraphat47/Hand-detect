import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

webcam = cv2.VideoCapture(0)
image = webcam.read()
image = webcam.read()
mp_draw = mp.solutions.drawing_utils
while True:
 success, image = webcam.read()    
 image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
 results = hands.process(image_rgb)
 
 print(results.multi_hand_landmarks)
 if results.multi_hand_landmarks:
    for landmark in results.multi_hand_landmarks:
      mp_draw.draw_landmarks(image, landmark,mp_hands.HAND_CONNECTIONS)   
 
 cv2.imshow("Webcam",image)
 cv2.waitKey(1)

image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
results = hands.process(image_rgb)
print(results.multi_hand_landmarks) 






