import cv2
import time
import math

centerbasket1 = 530
centerbasket2 = 300
xs = []
ys = []

vid = cv2.VideoCapture("bb3.mp4")

tracker = cv2.TrackerCSRT_create()
ret, img = vid.read()
box = cv2.selectROI("Tracking", img, False)

tracker.init(img, box)
print(box)

def drawBox(img, box):
    x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255,0,255), 3, 1)
    cv2.putText(img, "Tracking", (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

def goal_track(img, box):
    x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    centerball1 = x + int(w/2)
    centerball2 = y + int(h/2)
    cv2.circle(img, (centerball1, centerball2), 2, (0,0,255), 5)

    cv2.circle(img, (int(centerbasket1), int(centerbasket2)), 2, (0,0,255), 3)
    
    dist = math.sqrt(((centerball1-centerbasket1)**2)+ (centerball2-centerbasket2)**2)
    print(dist)

    if(dist <= 20):
        cv2.putText(img, "Basket!!!", (300, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    xs.append(centerball1)
    ys.append(centerball2)

    for i in range(len(xs)-1):
        cv2.circle(img, (xs[i], ys[i]), 2, (0,0,255), 5)

while True:
    check, img = vid.read()
    success, box = tracker.update(img)
    
    if(success):
        drawBox(img, box)
    else:
        cv2.putText(img, "Lost", (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    
    goal_track(img, box)

    cv2.imshow("Result", img)

    key = cv2.waitKey(25)
    if( key == 32):
        print("stop")
        break;
       
vid.release()
cv2.destroyAllWindows()