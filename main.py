import cv2

# Loads the dataset
cascade = cv2.CascadeClassifier('dataset.xml')

# Captures webcam info
cap = cv2.VideoCapture(0)

while True:
    # Sets fps to 60, not even sure if this does anything tbh
    cap.set(cv2.CAP_PROP_FPS, 60)

    # Reads each frame of the video stream and outlines where face is
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 4)

    # Draws rectangle and adds text around detected face
    for (x, y, w, h) in faces:
        cv2.putText(img, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)

    # Creates the GUI
    cv2.imshow('Facial Recognition', img)
    cv2.moveWindow('Facial Recognition', 60, 0)

    # When esc is pressed stop the program
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Exit stuff
cap.release()