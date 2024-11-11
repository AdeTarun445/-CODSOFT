import cv2
# Load the pre_traines Haar cascade face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture object
cap = cv2.VideoCapture(0) # 0 represents the default camera (usually webcam)

while True:
    # capture frame-by-frame
    ret, frame = cap.read()

    # convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5,minSize=(30,30))

    # Draw rectangles around the faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w , y+h), (255, 0, 0), 2)
    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)

    # exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()