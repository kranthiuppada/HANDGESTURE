# ✋ Gesture-Controlled App Launcher

This project uses **MediaPipe** and **OpenCV** to recognize simple hand gestures from your webcam and open apps or websites automatically.  
By pinching your thumb and index finger and drawing in the air, the system detects motion patterns and launches the mapped app.

---

## 🚀 Features
- Real-time hand tracking using MediaPipe.
- Pinch gesture detection to start drawing.
- Simple shape-based recognition (aspect ratio & stroke length).
- Automatically opens apps like YouTube, Netflix, WhatsApp, Spotify, etc.
- Live visual feedback on an on-screen canvas.

---

## 🧩 Requirements
```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ How to Run
1. Save the Python file (e.g., `gesture_launcher.py`).
2. Run the program:
   ```bash
   python gesture_launcher.py
   ```
3. Allow webcam access.
4. Pinch (thumb + index finger) to draw a shape in the air.
5. Release to trigger app recognition and open the mapped app.

---

## 💡 Gesture to App Mapping
| Gesture Shape | Heuristic Description | Opens |
|----------------|------------------------|--------|
| Wide drawing (aspect_ratio > 1.5) | Horizontal gesture | YouTube |
| Tall drawing (aspect_ratio < 0.5) | Vertical gesture | Netflix |
| Big strokes (height > 150) | Large gesture | WhatsApp |
| Long continuous drawing | Many points | Spotify |
| Default / others | Random small gesture | Hotstar |

---

## ⚙️ Controls
- **q** → Quit the application  
- **c** → Clear the drawing canvas  

---

## 🌐 Supported Apps
| Key | Application |
|-----|--------------|
| N | Netflix |
| Y | YouTube |
| W | WhatsApp Web |
| S | Spotify |
| J | Hotstar |
| C | Calculator |
| E | File Explorer |

---

## 🧠 Future Improvements
- Integrate a machine learning model for accurate gesture recognition.  
- Allow users to configure custom gestures and app mappings.  
- Add support for multiple hands or multi-finger gestures.  
- Improve UI overlay and visual tracking.

---

## 📸 Example Workflow
1. Start the script.  
2. Bring your hand in front of the webcam.  
3. Pinch (thumb + index finger) and draw in the air.  
4. Release the pinch — the app will open based on your gesture.  

---

## 🧑‍💻 Author
**Kranthi Uppada**  
*Tech Stack:* Python, OpenCV, MediaPipe  
*Description:* Gesture-based App Launcher for Human-Computer Interaction
