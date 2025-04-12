# Raspberry-Face-Recognition
#Use Python and Open CV to recognize multi face and show the name
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
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
rec=cv2.face.createLBPHFaceRecognizer()
rec.load(&quot;/home/pi/project/trainer/trainer.yml&quot;)
id=0
s=0
u=0
ri=0

50

ra=0
#open text file from attendance folder in mode specified
f=open(&#39;/home/pi/project/attendance/attendance.txt&#39;,&#39;w&#39;)
print(&quot;Students Present: &quot;)
for frame in camera.capture_continuous(rawCapture,
format=&quot;bgr&quot;, use_video_port=True):
# grab the raw NumPy array representing the image,
then initialize the timestamp
# and occupied/unoccupied text
image = frame.array
face_cascade =
cv2.CascadeClassifier(&#39;/home/pi/Downloads/project/haarcasca
de_frontalface_alt.xml&#39;)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
for (x, y, w, h) in faces:
cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
id,conf=rec.predict(gray[y:y+h,x:x+w])
if(id==1):
s+=1
if(s&lt;2):
print(&quot;Surya&quot;)
f.write(&#39;Surya\n&#39;)
f.flush()
else:
break
elif(id==2):
u+=1
if(u&lt;2):
print(&quot;Umar&quot;)
f.write(&#39;Umar\n&#39; )
f.flush()

51

else:
break
elif(id==3):
ri+=1
if(ri&lt;2):
print(&quot;Ritesh&quot;)
f.write( &#39;Ritesh\n&#39; )
f.flush()
else:
break
elif(id==4):
ra+=1
if(ra&lt;2):
print(&quot;Rahul&quot;)
f.write(&#39;Rahul\n&#39;)
f.flush()
else:
break
cv2.imshow(&quot;Frame&quot;, image)
key = cv2.waitKey(1) &amp; 0xFF
if(key == ord(&#39;q&#39;)):
break
rawCapture.truncate(0)
camera.close()
cv2.destroyAllWindows()
f.close()
print(&quot;Saved Attendance to attendance.txt&quot;)
