# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:54:52 2019

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:23:56 2019

@author: Admin
"""

import cv2
import imutils
import numpy as np

# Load the Haar cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
blue = []
red = []
green = []
hue = []
saturation = []
value = []
# Define function that will do detection
def detect(gray, frame):
  """ Input = greyscale image or frame from video stream
      Output = Image with rectangle box in the face
  """
  # Now get the tuples that detect the faces using above cascade
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  # faces are the tuples of 4 numbers
  # x,y => upperleft corner coordinates of face
  # width(w) of rectangle in the face
  # height(h) of rectangle in the face
  # grey means the input image to the detector
  # 1.3 is the kernel size or size of image reduced when applying the detection
  # 5 is the number of neighbors after which we accept that is a face
  
  # Now iterate over the faces and detect eyes
  for (x,y,w,h) in faces:
    #cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    # Arguements => image, top-left coordinates, bottomright coordinates, color, rectangle border thickness
    
    # we now need two region of interests(ROI) grey and color for eyes one to detect and another to draw rectangle
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    # Detect eyes now
    eyes = eyes_cascade.detectMultiScale(roi_gray, 1.1, 3)
    # Now draw rectangle over the eyes
    for (ex, ey, ew, eh) in eyes:
      #cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
      hx=ex
      hy=ey-30
      hw=ex+ew
      hh=ey+eh-30
        #cv2.rectangle(roi_color,(ex,ey-30),(ex+ew,ey+eh-30),(0,0,255),2)
    try:
        #cv2.rectangle(roi_color,(hx-15,hy-20),((2*hw)+45,hh-30),(0,0,255),2)
        roi = roi_color[hy-20:hh-30,hx-15:(2*hw)+45]
        cv2.imshow("roi",roi)
        b,g,r = cv2.split(roi)
        bl = np.mean(b)
        re = np.mean(r)
        gr = np.mean(g)
        blue.append(bl)
        red.append(re)
        green.append(gr)
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        h, s, v = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]
        hu = np.mean(h)
        sa = np.mean(s)
        va = np.mean(v)
        hue.append(hu)
        saturation.append(sa)
        value.append(va)
        # set blue and green channels to 0
        print(bl)
        print(gr)
        print(re)
        cv2.imshow("blue",b)
        cv2.imshow("red",r)
        cv2.imshow("green",g)
        return roi
    except UnboundLocalError:
        pass
    except:
        pass
  #return frame
    
# Capture video from webcam 
video_capture = cv2.VideoCapture("newdata6.mp4")
#video_capture.set(cv2.CV_CAP_PROP_FPS,60)
# Run the infinite loop
ret = True

while ret:
  try:
  # Read each frame
      ret, frame = video_capture.read()
      #print(frame.shape)
    #  if frame.empty():
    #      break;
      
      frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
      frame = imutils.rotate_bound(frame,90)
      # Convert frame to grey because cascading only works with greyscale image
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      # Call the detect function with grey image and colored frame
      canvas = detect(gray, frame)
      # Show the image in the screen
      #cv2.imshow("Video", canvas)
     # cv2.waitKey(1)
    #  if ret == False:
    #      break
     # Put the condition which triggers the end of program
    
    
      if cv2.waitKey(1) and 0xFF == ord('q'):
        break
  except AttributeError:
      break      
video_capture.release()
cv2.destroyAllWindows()

a = open("red.txt","wb") 
a.close()
with open("red.txt", "w+") as t:
    for x in red:
        t.write(str(x) + ",")

a = open("blue.txt","wb") 
a.close()
with open("blue.txt", "w+") as t:
    for x in blue:
        t.write(str(x) + ",")

a = open("green.txt","wb") 
a.close()
with open("green.txt", "w+") as t:
    for x in green:
        t.write(str(x) + ",")

a = open("hue.txt","wb") 
a.close()
with open("hue.txt", "w+") as t:
    for x in hue:
        t.write(str(x) + ",")

a = open("saturation.txt","wb") 
a.close()
with open("saturation.txt", "w+") as t:
    for x in saturation:
        t.write(str(x) + ",")

a = open("value.txt","wb") 
a.close()
with open("value.txt", "w+") as t:
    for x in value:
        t.write(str(x) + ",")