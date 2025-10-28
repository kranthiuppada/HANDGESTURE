import cv2
import mediapipe as mp
import numpy as np
import os
import math
import webbrowser

# Mediapipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Webcam setup
cap = cv2.VideoCapture(0)
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# App mapping
apps = {
    "N": "https://www.netflix.com",
    "Y": "https://www.youtube.com",
    "W": "https://web.whatsapp.com",
    "S": "spotify",
    "J": "https://www.hotstar.com",
    "C": "calc",
    "E": "explorer"
}

def open_app(letter):
    if letter in apps:
        app = apps[letter]
        if app.startswith("http"):
            webbrowser.open(app)   # open in default browser (Chrome if default)
        else:
            os.system(app)
        print(f"Opening {app}...")
    else:
        print(f"No app assigned for {letter}")

# Helper to calculate distance between two points
def distance(p1, p2):
    if p1 is None or p2 is None:
        return float('inf')
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    drawing = False
    points = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # Thumb tip and index tip
                thumb_tip = (int(landmarks.landmark[4].x * w),
                             int(landmarks.landmark[4].y * h))
                index_tip = (int(landmarks.landmark[8].x * w),
                             int(landmarks.landmark[8].y * h))

                # Draw landmarks
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

                # Check pinch (distance < threshold)
                if distance(thumb_tip, index_tip) < 40:
                    drawing = True
                    points.append(index_tip)
                else:
                    # When pinch released, recognize letter
                    if drawing and len(points) > 5:
                        xs = [p[0] for p in points]
                        ys = [p[1] for p in points]
                        aspect_ratio = (max(xs)-min(xs)) / max(1, (max(ys)-min(ys)))
                        height = max(ys) - min(ys)

                        # Simple heuristic-based classification
                        if aspect_ratio > 1.5:
                            letter = "Y"   # wide → Y (YouTube)
                        elif aspect_ratio < 0.5:
                            letter = "N"   # tall → N (Netflix)
                        elif height > 150:
                            letter = "W"   # big strokes → W (WhatsApp)
                        elif len(points) > 100:
                            letter = "S"   # longer drawing → Spotify
                        else:
                            letter = "J"   # default → Hotstar

                        print("👉 Recognized Letter:", letter)
                        open_app(letter)
                        points = []

                    drawing = False

                # Draw line on canvas
                for i in range(1, len(points)):
                    cv2.line(canvas, points[i-1], points[i], (255, 255, 255), 5)

        combined = cv2.addWeighted(frame, 1, canvas, 1, 0)
        cv2.imshow("Pinch to Draw", combined)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            canvas[:] = 0
            points = []

cap.release()
cv2.destroyAllWindows()