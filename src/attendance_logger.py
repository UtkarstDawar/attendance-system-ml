import csv
import os
from datetime import datetime, time

ATTENDANCE_DIR = "attendance"
ATTENDANCE_FILE = os.path.join(ATTENDANCE_DIR, "attendance.csv")

# Attendance allowed time window
START_TIME = time(9, 30)   # 9:30 AM
END_TIME = time(10, 0)     # 10:00 AM


def mark_attendance(student_id, emotion):
    """
    Marks attendance for a student with emotion, date, and time.
    Attendance is only marked within the allowed time window.
    """

    now = datetime.now()
    current_time = now.time()

    # Check time window
    if not (START_TIME <= current_time <= END_TIME):
        print("Outside attendance time window")
        return

    # Create attendance directory if not exists
    os.makedirs(ATTENDANCE_DIR, exist_ok=True)

    file_exists = os.path.isfile(ATTENDANCE_FILE)

    # Write attendance
    with open(ATTENDANCE_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header if file is new
        if not file_exists:
            writer.writerow(["student_id", "emotion", "date", "time"])

        writer.writerow([
            student_id,
            emotion,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S")
        ])

    print(f"Attendance marked: {{'student_id': '{student_id}', "
          f"'emotion': '{emotion}', "
          f"'date': '{now.strftime('%Y-%m-%d')}', "
          f"'time': '{now.strftime('%H:%M:%S')}'}}")