import cv2
import pickle
import numpy as np
from insightface.app import FaceAnalysis
from deepface import DeepFace
from attendance_logger import mark_attendance

# ---------------- CONFIG ----------------
EMBEDDINGS_PATH = "models/embeddings.pkl"
THRESHOLD = 0.5  # cosine similarity threshold
# ---------------------------------------

# Load stored embeddings
with open(EMBEDDINGS_PATH, "rb") as f:
    db = pickle.load(f)

# Initialize InsightFace
app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

cap = cv2.VideoCapture(0)
marked_today = set()

print("Starting Attendance System with Emotion Detection...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = app.get(frame)

    for face in faces:
        emb = face.embedding
        best_match = None
        best_score = -1

        # Compare embeddings
        for item in db:
            score = cosine_similarity(emb, item["embedding"])
            if score > best_score:
                best_score = score
                best_match = item["student_id"]

        x1, y1, x2, y2 = map(int, face.bbox)

        # -------- Emotion Detection --------
        face_img = frame[y1:y2, x1:x2]
        try:
            emotion_result = DeepFace.analyze(
                face_img,
                actions=["emotion"],
                enforce_detection=False
            )
            emotion = emotion_result[0]["dominant_emotion"]
        except:
            emotion = "unknown"
        # ----------------------------------

        if best_score > THRESHOLD:
            label = f"{best_match} | {emotion}"

            if best_match not in marked_today:
                mark_attendance(best_match, emotion)
                marked_today.add(best_match)
        else:
            label = "Unknown"

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()