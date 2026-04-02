import cv2
import os

# Create folder to store faces
if not os.path.exists("faces"):
    os.makedirs("faces")

cap = cv2.VideoCapture(0)

student_name = input("Enter student name: ")

count = 0

while True:
    ret, frame = cap.read()

    cv2.imshow("Capture Face", frame)

    key = cv2.waitKey(1)

    # Press 's' to save image
    if key == ord('s'):
        img_name = f"faces/{student_name}_{count}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Saved: {img_name}")
        count += 1

    # Press ESC to exit
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()