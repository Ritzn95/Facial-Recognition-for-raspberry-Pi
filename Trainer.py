import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.createLBPHFaceRecognizer()
detector=
cv2.CascadeClassifier(&quot;haarcascade_frontalface_alt.xml&quot;);

def getImagesAndLabels(path):
#get the path of all the files in the folder
imagePaths=[os.path.join(path,f) for f in
os.listdir(path)]
#create empth face list
faceSamples=[]
#create empty ID list
Ids=[]
#now looping through all the image paths and loading
the Ids and the images
for imagePath in imagePaths:
#loading the image and converting it to gray scale
pilImage=Image.open(imagePath).convert(&#39;L&#39;)
#Now we are converting the PIL image into numpy
array
imageNp=np.array(pilImage,&#39;uint8&#39;)
#getting the Id from the image
Id=int(os.path.split(imagePath)[-1].split(&quot;.&quot;)[1])
# extract the face from the training image sample
faces=detector.detectMultiScale(imageNp)

53
#If a face is there then append that in the list as
well as Id of it
for (x,y,w,h) in faces:
faceSamples.append(imageNp[y:y+h,x:x+w])
Ids.append(Id)
cv2.imshow(&quot;Training&quot;, imageNp)
cv2.waitKey(10)
return faceSamples,Ids

faces,Ids = getImagesAndLabels(&#39;dataset&#39;)
recognizer.train(faces, np.array(Ids))
recognizer.save(&#39;trainer/trainer.yml&#39;)
print(&quot;Training For Faces Complete!&quot;)
print(&quot;EZ&quot;)
cv2.destroyAllWindows()
