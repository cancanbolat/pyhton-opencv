import cv2

vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("D:\\OpenCV\\haarCascade\\face.xml")


while 1:
    _,frame = vid.read()#1
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.6,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("video-face",frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()


