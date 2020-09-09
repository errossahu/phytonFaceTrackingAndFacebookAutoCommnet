import cv2
cam = cv2.VideoCapture(0)
cam.set(3,648) #ubah Lebar Cam
cam.set(4,480)
faceDetector =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeDetector= cv2.CascadeClassifier('haarcascade_eye.xml')
wAbu = 0 ;
eyes= 0 ;
while True:
    retV, frame = cam.read()

    abu=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = faceDetector.detectMultiScale(abu,1.3, 5)
    for(x,y,w,h) in face:
        frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        wAbu= abu[y:y+h ,x:x+w]
        wwarna= frame[y:y+h, x:x+w]
        eyes= eyeDetector.detectMultiScale(wAbu)
    for(xe , ye , we , he) in eyes:
        cv2.rectangle(wwarna,(xe,ye),(xe+we, ye+he),(0,0,255),1)
        cv2.imshow('WEBCAMKU', frame)
    # cv2.imshow('webcamku',abu)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

        cam.release()
        cv2.destroyAllWindows()

