import os
import pickle
import cv2
import numpy as np
from insightface.app import FaceAnalysis

DATA_DIR = "data"
OUTPUT_PATH = "models/embeddings.pkl"

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)

embeddings = []

for student_id in os.listdir(DATA_DIR):
    student_path = os.path.join(DATA_DIR, student_id)

    if not os.path.isdir(student_path):
        continue

    for img_name in os.listdir(student_path):
        img_path = os.path.join(student_path, img_name)

        img = cv2.imread(img_path)
        if img is None:
            continue

        faces = app.get(img)

        if len(faces) != 1:
            continue  # skip unclear images

        emb = faces[0].embedding
        embeddings.append({
            "student_id": student_id,
            "embedding": emb
        })

print(f"Total embeddings extracted: {len(embeddings)}")

os.makedirs("models", exist_ok=True)
with open(OUTPUT_PATH, "wb") as f:
    pickle.dump(embeddings, f)

print("Embeddings saved to models/embeddings.pkl")