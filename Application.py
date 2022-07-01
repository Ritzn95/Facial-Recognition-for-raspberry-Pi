#Use Python and Open CV to recognize multi face
#Sample to get video from PiCam
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys

# initialize the camera and grab a reference to the raw
camera capture
camera = PiCamera()

54

camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
face_id = 1
while(face_id &gt; 0):
face_id=input(&#39;Enter ID:&#39;)
count=0
while(True):

# capture frames from the camera

for frame in

camera.capture_continuous(rawCapture, format=&quot;bgr&quot;,
use_video_port=True):
# grab the raw NumPy array representing the image,
then initialize the timestamp
# and occupied/unoccupied text
image = frame.array
#load defined classifier with path
face_cascade =

cv2.CascadeClassifier(&#39;/home/pi/project/haarcascade_frontal
face_alt.xml&#39;)

gray =

cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,

1.1, 5)

for (x, y, w, h) in faces:

cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

count += 1
if count&gt;20:

55
print (&quot;Dataset for ID:&quot;, face_id,

&quot;created successfully&quot;)

cv2.destroyAllWindows()
sys.exit()
cv2.imwrite(&quot;dataset/User.&quot; +

str(face_id) + &#39;.&#39; + str(count) + &quot;.jpg&quot;,gray[y:y+h,x:x+w])
# show the frame

cv2.imshow(&quot;Frame&quot;, image)
key = cv2.waitKey(1) &amp; 0xFF

# clear the stream in preparation for the next frame

rawCapture.truncate(0)
