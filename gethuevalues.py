
import cv2
import numpy as np
from scipy import signal
cap = cv2.VideoCapture(0)

hue = []
saturation = []
value = []



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]
    hu = np.mean(h)
    sa = np.mean(s)
    va = np.mean(v)
    hue.append(hu)
    saturation.append(sa)
    value.append(va)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
