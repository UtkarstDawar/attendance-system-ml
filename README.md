# Attendance System using Face Recognition

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Results](#results)
- [Notes](#notes)
- [Future Improvements](#future-improvements)

---

## Project Overview
This project implements an **automated attendance system** using **face recognition**.  
Key features:
- Detects faces in real-time using **InsightFace (ArcFace embeddings)**  
- Recognizes student identities  
- Marks attendance **only during a specified time window (9:30 AM – 10:00 AM)**  
- Stores attendance data in a **CSV file with timestamps**  

This system is **internship-ready** and demonstrates real-world ML pipeline implementation.

---

## Dataset
- Self-collected images of students  
- Each student has **15–30 images** captured under different angles, expressions, and lighting  
- Folder structure:data/
├── S001/
├── S002/
└── …
---

## Methodology
1. **Face Detection:** Real-time detection using `InsightFace`.  
2. **Face Embeddings:** Generate ArcFace embeddings for each student image.  
3. **Recognition:** Compute **cosine similarity** between live face embeddings and stored embeddings.  
4. **Attendance Logging:**  
   - Marks attendance **once per student**  
   - Marks attendance **only during 9:30–10:00 AM**  
   - Saves attendance to `attendance/attendance.csv`  

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/UtkarstDawar/attendance-system-ml.git
cd attendance-system-ml
2. Install required packages:
pip install -r requirements.txt
requirements.txt includes: numpy, opencv-python, insightface, onnxruntime

How to Run
	1.	Capture student images (if not already done):
    python3 src/capture_images.py
    2.	Extract embeddings:
    python3 src/extract_embeddings.py
    3.	Run real-time recognition and mark attendance:
    python3 src/recognize_and_mark.py
    	•	Press q to quit the webcam
Results
	•	Detects faces and recognizes students in real-time
	•	Marks attendance with student ID, date, and time
	•	Time-based attendance restriction works correctly
	•	Example attendance log:
                                student_id,emotion,date,time
                                S001,unknown,2025-12-30,09:41:12
                                S002,unknown,2025-12-30,09:42:08
Notes
	•	Do not push models/embeddings.pkl to GitHub (it’s large).
	•	Embeddings can be regenerated locally using extract_embeddings.py
	•	Tested on macOS with Python 3.9+
	•	Project demonstrates:
	•	Real-time ML pipeline
	•	Time-restricted automation
	•	Industry-grade embeddings
    
Future Improvements
	•	Emotion detection using FER2013 / DeepFace
	•	Accuracy / confusion matrix visualization
	•	Baseline vs ArcFace comparison
	•	GUI for easier interaction
	•	Cloud or mobile deployment for real-time streaming

                                    
