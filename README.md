# Hand Gesture Recognition 
A collection of Python projects using **Mediapipe (0.10.5)** and **OpenCV** for real-time hand tracking, gesture recognition, volume control, and finger counting.

---

## Features
- Real-time hand tracking with Mediapipe
- Volume control using finger distance (Pycaw)
- Finger counting (number detection)
- Modular hand tracking class for reuse

---

## Requirements
- Python 3.9
- Mediapipe 0.10.5
- OpenCV
- NumPy
- Pycaw (Windows audio control)

---

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/HandGesture-Recognition.git
   cd HandGesture-Recognition
```

2. Create a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # macOS/Linux
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Run any script:
```bash
   python handgesture.py
   python volume_control.py
   python number_detection.py
```
