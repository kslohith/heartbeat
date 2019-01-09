'''Image face detection'''

import cv2,time
img = cv2.imread("face.jpg",1)
img = cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2)))
#print(img.shape)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5)
for x,y,w,h in faces:
    print(x,y,w,h)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)

cv2.imshow("Face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''Video face detection'''

import cv2,time
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
video = cv2.VideoCapture(0)
a = 0
while True:
    a=a+1
    check,frame = video.read()
    #print(check)
    #print(frame)
    grey_vid = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey_vid, scaleFactor=1.05, minNeighbors=5)
    for x,y,w,h in faces:
        #print(x,y,w,h)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = grey_vid[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.05, minNeighbors=5)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
            hx=ex
            hy=ey-30
            hw=ex+ew
            hh=ey+eh-30
            #cv2.rectangle(roi_color,(ex,ey-30),(ex+ew,ey+eh-30),(0,0,255),2)
        
        cv2.rectangle(roi_color,(hx,hy),(hw,hh),(0,0,255),2)
    cv2.imshow("Video",frame)
    key = cv2.waitKey(1)
    
    if(key == ord('q')):
        break

print(a)
#time.sleep(3)

video.release()
cv2.destroyAllWindows()
