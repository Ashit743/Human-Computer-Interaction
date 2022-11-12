from cv2 import cv2 as cv
import handTrackingModule as htm
import time as t
from termcolor import colored,cprint
from datetime import datetime as dt



print(colored("Connection Successfull!",'green'))

cprint('Opening..','green',attrs=['blink'])
#setting speeds for motors
Speedarrr = [0.2,0.4,1]
# Initializing the modules
cap = cv.VideoCapture(0)
detect = htm.HandDetector(maxHands=1)

# Make this True to count the left hand
_LEFT_HAND = False
# Initializing the finger tips
tipIDs = [4, 8, 12, 16, 20]
now = dt.now()
tempC = 24
def dispTemperature(frame,tempC):
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame, f'Temperature: {tempC}', (0, 70), font, 1, (36, 255, 12), 2)

def drawNumber(frame, noFinger):
    font = cv.FONT_HERSHEY_SIMPLEX
    text = str(noFinger)
    cv.putText(frame, text, (0, 470), font, 2, (36, 255, 12), 3)
    if noFinger>3:
        cv.putText(frame,"laddle Control",(100,470),font,2,(255,255,255),2)
    else:
        cv.putText(frame,"Motor Control",(100,470),font,2,(255,255,255),2)


while (cap.isOpened()):
    isSuccess, frame = cap.read()

    if isSuccess:
        frame = detect.findHands(frame)
        # Fliping the frame horrizontally
        frame = cv.flip(frame, 1)

        lmList_1 = detect.findPosition(frame, handNo=0, boxDraw=False)
        fW = cap.get(3)
        fH = cap.get(4)
        # Checking the Finger of Hand 1
        if len(lmList_1) != 0:
            fingerCheck = []

            if not _LEFT_HAND:
                # For thumb
                if lmList_1[4][1] > lmList_1[3][1]:
                    fingerCheck.append(True)
                else:
                    fingerCheck.append(False)
            else:
                # For thumb
                if lmList_1[4][1] < lmList_1[3][1]:
                    fingerCheck.append(True)
                else:
                    fingerCheck.append(False)

            # For other fngers
            for id in range(1, 5):
                if lmList_1[tipIDs[id]][2] < lmList_1[tipIDs[id] - 2][2]:
                    fingerCheck.append(True)
                else:
                    fingerCheck.append(False)

            totalFingers = fingerCheck.count(True)

            #print(totalFingers)
            drawNumber(frame, totalFingers)
        after = dt.now()
        tt = (after - now).total_seconds()
        if (tt) > 2: #display every 1s
            tempC = 24
            now = after
        # Calculating the FPS
        detect.addFPS(frame)
        dispTemperature(frame,tempC)
        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv.destroyAllWindows()
