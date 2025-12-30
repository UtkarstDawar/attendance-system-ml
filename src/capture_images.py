import cv2
import os

# Change this to the student ID or name
student_id = input("Enter student ID (e.g., S001): ")
num_images = int(input("How many images to capture? "))

# Create folder for student if it doesn't exist
save_dir = os.path.join("data", student_id)
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

print("Press 'c' to capture an image. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Images", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        count += 1
        filename = os.path.join(save_dir, f"{student_id}_{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Captured {filename}")

        if count >= num_images:
            print("Done capturing images.")
            break

    elif key == ord('q'):
        print("Quitting without finishing capture.")
        break

cap.release()
cv2.destroyAllWindows()