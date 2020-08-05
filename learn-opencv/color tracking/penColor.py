import numpy as np
import cv2

# cap = cv2.VideoCapture('H:/Github/OpenCv/Research/videos/pen.mp4')
cap = cv2.VideoCapture(0)

kernel = np.ones((3,3),np.uint8)
kernelSmooth = np.ones( (25,25),np.float32 ) / 625

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 1,
                        qualityLevel = 0.8,
                        minDistance = 7,
                        blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,4))
  
# Take first frame and find corners in it
ret, old_frame = cap.read()
hsv =  cv2.cvtColor(old_frame,cv2.COLOR_BGR2HSV)

# index 0= Hue 1= sat 2=value
lower_limit = np.array([30,150,50])
upper_limit = np.array([255,255,180])
# inRnage Funtion will return 1 if the color is present range
mask = cv2.inRange(hsv,lower_limit,upper_limit)

# 2 frames are passed mask values will applied to 2nd frame and bitwise op
res = cv2.bitwise_and(old_frame,old_frame,mask = mask)


old_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
# cv2.imshow("s" , old_gray )
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
print(p0)
# Create a mask image for drawing purposes
old_mask = np.zeros_like(old_frame)


while(1):
    
    ret,frame = cap.read()
    smoothed = cv2.filter2D(frame,-1,kernelSmooth)
    hsv =  cv2.cvtColor(smoothed,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower_limit,upper_limit)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    frame_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    
    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    if p1 is None:
       #p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
       p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    good_new = p1[st==1]
    good_old = p0[st==1]

    
    color = [0, 155, 31,1]  
    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
       a,b = new.ravel()
       c,d = old.ravel()
          
       old_mask = cv2.line(old_mask, (a,b),(c,d), color, 5)
       frame = cv2.circle(frame,(a,b),5,color,-1)
       img = cv2.add(frame,old_mask)
       img = cv2.flip(img,1)
       cv2.imshow('frame',img)
       cv2.imshow('res',res)
   
       
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

  
    if cv2.waitKey(27) & 0xFF == ord('q'):
         break
 
cv2.destroyAllWindows()
cap.release()
