from datetime import datetime
import pandas as pd
import os

CSV_PATH = "results/attendance.csv"

def mark_attendance(student_id, emotion):
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    if current_time < "09:30" or current_time > "10:00":
        print("Outside attendance time window")
        return

    os.makedirs("results", exist_ok=True)

    row = {
        "student_id": student_id,
        "emotion": emotion,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S")
    }

    df = pd.DataFrame([row])

    if not os.path.exists(CSV_PATH):
        df.to_csv(CSV_PATH, index=False)
    else:
        df.to_csv(CSV_PATH, mode="a", header=False, index=False)

    print("Attendance marked:", row)

if __name__ == "__main__":
    mark_attendance("S001", "neutral")