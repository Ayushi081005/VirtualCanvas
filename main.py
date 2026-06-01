import cv2
import numpy as np
import mediapipe as mp
import pyttsx3
import config
from canvas import create_canvas

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

engine = pyttsx3.init()
engine.say("Virtual Canvas Activated. Show your hand to draw.")
engine.runAndWait()

canvas = create_canvas(config.FRAME_WIDTH, config.FRAME_HEIGHT)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            h, w, _ = frame.shape
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            cv2.circle(canvas, (x, y), config.BRUSH_RADIUS, config.BRUSH_COLOR, -1)

    # Resize canvas to match frame size just in case
    if canvas.shape[:2] != frame.shape[:2]:
        canvas = cv2.resize(canvas, (frame.shape[1], frame.shape[0]))

    combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.imshow("Virtual Canvas", combined)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

