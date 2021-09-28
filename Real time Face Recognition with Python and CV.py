#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import cv2
import os


# In[3]:


#initialize classifier
cascPath = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


# In[25]:


#apply faceCascade on webcam frames

video_capture = cv2.VideoCapture(0)

while True:
    #capture frame by frame
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), 
                                         flags = cv2.CASCADE_SCALE_IMAGE)
    
    #draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    #display the resulting frame
    cv2.imshow('Video', frames)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# In[26]:


cv2.destroyAllWindows()
video_capture.release()


# In[ ]:





# In[ ]:




