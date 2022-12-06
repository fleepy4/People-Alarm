import cv2
import db
import os
from bot_files import sender
face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
stop = 0
while True:
    status, pic = cap.read()
    img_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
    for (x, y, w, h) in faces:
        cv2.rectangle(pic, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if db.is_active():
            cv2.imwrite("bot_files/temp/save.png", pic)
            sender.sender()
            db.change_status()
            os.remove("bot_files/temp/save.png")

    cv2.imshow('rez', pic)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
