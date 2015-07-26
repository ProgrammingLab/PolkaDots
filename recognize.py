import cv2
import sys

cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml"
#cascade_path = "TrainingAssistant/pan2/cascade.xml"
#cascade_path = "bikini.xml"

argvs = sys.argv
if (len(argvs) != 2):
    print 'Usage: # python %s filename' % argvs[0]
    quit()

image_path = argvs[1] 
image_name = image_path[4:]
try:
    img = cv2.imread(image_path, 1)
except:
    print 'faild to load %s' % image_path
    quit()

color = (255, 255, 255)
image = cv2.imread(image_path)
image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_path)

facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

print facerect

if len(facerect) > 0:
    for rect in facerect:
        cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

    cv2.imwrite("detected/detected_"+image_name, image)
