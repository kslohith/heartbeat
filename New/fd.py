# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:47:09 2019

@author: Dell
"""

import cv2
import imutils

# Load the Haar cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

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
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    # Arguements => image, top-left coordinates, bottomright coordinates, color, rectangle border thickness
    
    # we now need two region of interests(ROI) grey and color for eyes one to detect and another to draw rectangle
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    # Detect eyes now
    eyes = eyes_cascade.detectMultiScale(roi_gray, 1.1, 3)
    # Now draw rectangle over the eyes
    for (ex, ey, ew, eh) in eyes:
      cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
      hx=ex
      hy=ey-30
      hw=ex+ew
      hh=ey+eh-30
        #cv2.rectangle(roi_color,(ex,ey-30),(ex+ew,ey+eh-30),(0,0,255),2)
    try:
        cv2.rectangle(roi_color,(hx-15,hy-20),((2*hw)+45,hh-30),(0,0,255),2)
        roi = roi_color[hy-20:hh-30,hx-15:(2*hw)+45]   # Normal Case when both eyes are detected
#        roi = roi_color[hy-20:hh-30,hx-60:(2*hw)-40]
        cv2.imshow("roi",roi)
        #return roi
    except UnboundLocalError:
        pass
  return frame


frame = cv2.imread("Nidhi2.jpg")
frame = cv2.resize(frame,(int(frame.shape[1]/4),int(frame.shape[0]/4)))
#cv2.imshow("new",frame)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Call the detect function with grey image and colored frame
canvas = detect(gray, frame)
cv2.imshow("frame",canvas)
# Capture video from webcam 
#video_capture = cv2.VideoCapture("newdata.mp4")
# Run the infinite loop
#while True:
#  # Read each frame
#  _, frame = video_capture.read()
#  print(frame.shape)
#  

#  frame = imutils.rotate_bound(frame,90)
  # Convert frame to grey because cascading only works with greyscale image
#  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#  # Call the detect function with grey image and colored frame
#  canvas = detect(gray, frame)
#  # Show the image in the screen
#  cv2.imshow("Video", canvas)
#  # Put the condition which triggers the end of program
#  if cv2.waitKey(1) & 0xFF == ord('q'):
#    break
#video_capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
