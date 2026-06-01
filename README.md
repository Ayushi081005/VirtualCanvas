# Virtual Canvas 🎨🖐️

An interactive, AI-powered computer vision application that allows users to draw in mid-air using hand gestures. By tracking your hand movements via a webcam, this project turns your index finger into a virtual paintbrush.

---

## 🚀 Features

* **Real-time Hand Tracking:** Uses Google MediaPipe for ultra-low latency hand landmark detection.
* **Voice Assistance:** Integrated text-to-speech feedback using `pyttsx3` to notify you when the system activates.
* **Mirror-Mode Drawing:** Frames are flipped horizontally to provide an intuitive, mirror-like drawing experience.
* **Modular Architecture:** Configurations and canvas setups are separate for easy customization.

---

## 🛠️ Tech Stack

* **Python 3.x**
* **OpenCV:** For video capturing, frame processing, and drawing.
* **MediaPipe:** For AI-driven hand gesture tracking.
* **Pyttsx3:** For offline text-to-speech audio alerts.
* **NumPy:** For high-performance matrix manipulations on canvas layers.

---## 📋 Prerequisites & Installation

###
1. Clone the Repository
2. Install Dependencies
Make sure you have pip updated, then run:

Bash
pip install opencv-python numpy mediapipe pyttsx3

📂 Project Structure
├── canvas.py             # Helper script to initialize and manage the drawing canvas

├── config.py             # Global configurations (brush size, colors, screen dimensions)

├── draw_utils.py         # Utility functions for custom drawing operations/overlays

├── gesture_control.py    # Logic for recognizing specific hand gestures (e.g., erase, lift pen)

├── hand_tracking.py      # MediaPipe wrapper for detecting and extracting hand landmarks

├── main.py               # Application entry point containing the core execution loop

├── requirements.txt      # List of external Python dependencies for easy installation

└── voice_command.py      # Audio feedback and pyttsx3 text-to-speech engine controls


🎮 How to Use
Run the main script:

Bash
python main.py
Your webcam will turn on, and a voice will announce: "Virtual Canvas Activated. Show your hand to draw."

Raise your hand to the camera. The system will track your Index Finger Tip.

Move your finger around to draw on the screen!

Press q on your keyboard to exit the application.

🔮 Future Roadmap
[ ] Gesture Controls: Implement a mechanism to lift the pen (e.g., pinching fingers to stop drawing).

[ ] Color Palette: Add on-screen buttons to change brush colors dynamically in real-time.

[ ] Eraser Tool: Introduce an eraser gesture or a clear-screen shortcut.
