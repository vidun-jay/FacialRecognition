import cv2

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    cap.set(cv2.CAP_PROP_FPS, 60)
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)

    cv2.imshow('Facial Recognition', img)
    cv2.moveWindow('Facial Recognition', 60, 0)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()