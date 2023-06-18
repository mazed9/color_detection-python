import cv2
from PIL import Image
from util import get_limits


cap=cv2.VideoCapture(0)

yellow = [0, 255, 255]


while True:
    ret, frame= cap.read()

    hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(yellow)
    binary_mask= cv2.inRange(hsvimage,lowerLimit,upperLimit)

    mask= Image.fromarray(binary_mask)

    bbox=mask.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 =bbox

        frame=cv2.rectangle(frame, (x1, y1),(x2, y2), (0, 255, 0), 5)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

