import cv2
import numpy as np
# Params
maxArea = 150
minArea = 10
# Read image
I = cv2.imread('13.png')
# Convert to gray
Igray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
# Threshold
ret, Ithresh = cv2.threshold(Igray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# Keep only small components but not to small
comp = cv2.connectedComponentsWithStats(Ithresh)
labels = comp[1]
labelStats = comp[2]
labelAreas = labelStats[:,4]
for compLabel in range(1,comp[0],1):
    if labelAreas[compLabel] > maxArea or labelAreas[compLabel] < minArea:
        labels[labels==compLabel] = 0
labels[labels>0] =  1
# Do dilation
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(25,25))
IdilateText = cv2.morphologyEx(labels.astype(np.uint8),cv2.MORPH_DILATE,se)
# Find connected component again
comp = cv2.connectedComponentsWithStats(IdilateText)
# Draw a rectangle around the text
labels = comp[1]
labelStats = comp[2]
#labelAreas = labelStats[:,4]
for compLabel in range(1,comp[0],1):
    cv2.rectangle(I,(labelStats[compLabel,0],labelStats[compLabel,1]),(labelStats[compLabel,0]+labelStats[compLabel,2],labelStats[compLabel,1]+labelStats[compLabel,3]),(0,0,255),2)
cv2.imshow("img",I)
