import cv2
import pickle
import numpy as np
from insightface.app import FaceAnalysis
from attendance_logger import mark_attendance

EMBEDDINGS_PATH = "models/embeddings.pkl"
THRESHOLD = 0.5  # cosine similarity threshold

# Load embeddings
with open(EMBEDDINGS_PATH, "rb") as f:
    db = pickle.load(f)

# Initialize InsightFace
app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

cap = cv2.VideoCapture(0)
marked_today = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = app.get(frame)

    for face in faces:
        emb = face.embedding

        best_match = None
        best_score = -1

        for item in db:
            score = cosine_similarity(emb, item["embedding"])
            if score > best_score:
                best_score = score
                best_match = item["student_id"]

        x1, y1, x2, y2 = map(int, face.bbox)

        if best_score > THRESHOLD:
            label = f"{best_match} ({best_score:.2f})"

            # Avoid multiple marking
            if best_match not in marked_today:
                mark_attendance(best_match, "unknown")
                marked_today.add(best_match)
        else:
            label = "Unknown"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
