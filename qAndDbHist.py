from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import cv2

DatabaseAd = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/"
QueryAd = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/"

img = cv2.imread('/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/first001.png')
cv2.imshow('whatever',img)
# cv2.calcHist([img], [0], None, [256], [0,256])
# plt.hist(img.ravel(), 256, [0,256]);plt.show()
color = ('b', 'g', 'r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color = col)
    plt.xlim([0,256])
    print (i)
    print(histr)
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()


