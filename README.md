# Hand Gesture Recognition

A collection of Python projects using **Mediapipe (0.10.5)** and **OpenCV** for real-time hand tracking, gesture recognition, volume control, and finger counting.

---

## Overview

This project demonstrates the use of computer vision and machine learning libraries to detect and interpret hand gestures in real time using a standard webcam. It is designed for learning purposes and practical applications such as contactless control systems.

---

## Features

- Real-time hand tracking with Mediapipe
- Volume control using finger distance (Pycaw)
- Finger counting (number detection)
- Modular hand tracking class for reuse
- FPS display for performance monitoring
- Multi-hand detection support

---

## Learning Outcomes

By completing or studying this project, you will be able to:

- Understand how **Mediapipe** detects and tracks hand landmarks in real time
- Apply **OpenCV** for capturing webcam video, drawing overlays, and processing frames
- Calculate **Euclidean distance** between hand landmarks to measure finger spread
- Map physical gestures to system-level actions (e.g., audio volume via **Pycaw**)
- Build a **modular, reusable class** for hand tracking that can plug into any Python project
- Work with **NumPy** for efficient numerical computations on landmark coordinates
- Understand the **21-point hand landmark model** used by Mediapipe
- Debug and optimize real-time video processing pipelines
- Structure a Python project with clean separation of concerns

---

## Requirements

### Software
- Python 3.9
- Mediapipe 0.10.5
- OpenCV (`opencv-python`)
- NumPy
- Pycaw (Windows audio control)
- comtypes (required by Pycaw)

### Hardware
- Webcam (built-in or external)
- Windows OS (required for Pycaw volume control)
- Adequate lighting for hand detection

---

## Project Structure
```
HandGesture-Recognition/
│
├── handgesture.py          # Core hand tracking demo
├── volume_control.py       # Volume control using hand gestures
├── number_detection.py     # Finger counting / number detection
├── HandTrackingModule.py   # Reusable hand tracking class
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/yourusername/HandGesture-Recognition.git
   cd HandGesture-Recognition
```

2. **Create a virtual environment:**
```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

4. **Run any script:**
```bash
   python handgesture.py        # Basic hand tracking
   python volume_control.py     # Gesture-based volume control
   python number_detection.py   # Finger counting
```

---

## Usage

| Script | Description | Key Gesture |
|---|---|---|
| `handgesture.py` | Displays hand landmarks on screen | Any hand movement |
| `volume_control.py` | Controls system volume | Pinch thumb & index finger |
| `number_detection.py` | Counts raised fingers (0–5) | Raise fingers one by one |

---

## How It Works

1. **Webcam Feed** — OpenCV captures live video frames
2. **Hand Detection** — Mediapipe identifies hands and maps 21 landmarks per hand
3. **Gesture Interpretation** — Landmark coordinates are analysed (distances, angles, positions)
4. **Action Execution** — Results are used to control volume, count fingers, or trigger events

### Mediapipe 21-Point Hand Landmark Model
```
                 8   12  16  20
                 |   |   |   |
              7  |11  |15  |19
              |  |   |   |   |
           6  10  14  18
              \  |  /
               4 0
               |
               3
               |
               2
               |
               1
               |
               0  (WRIST)
```

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Webcam not detected | Check device index in `cv2.VideoCapture(0)` — try `1` or `2` |
| Mediapipe install fails | Ensure you are using Python 3.9 exactly |
| Pycaw not working | Pycaw only supports Windows; use a Windows machine |
| Low FPS / lag | Reduce frame resolution or close background apps |
| Hand not detected | Improve lighting and keep hand fully in frame |

---


## Acknowledgements

- [Mediapipe by Google](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/)
- [Pycaw](https://github.com/AndreMiras/pycaw)
