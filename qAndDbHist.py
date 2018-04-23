from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import cv2

DatabaseAd = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/"
QueryAd = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/"

# img = cv2.imread('/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/first001.png')
# cv2.imshow('whatever',img)
# cv2.calcHist([img], [0], None, [256], [0,256])
# plt.hist(img.ravel(), 256, [0,256]);plt.show()
# color = ('b', 'g', 'r')
# for i,col in enumerate(color):
#     histr = cv2.calcHist([img], [i], None, [256], [0,256])
#     plt.plot(histr, color = col)
#     plt.xlim([0,256])
#     print (i)
#     print(histr)
# hist = np.empty((3,256))
# plt.show()
hist0 = np.empty((256,256,256))
for folders in os.listdir(DatabaseAd+'traffic/'):
    if '.png' in folders:
        image = cv2.imread(DatabaseAd+'traffic/'+folders.title().lower())
        hist0 = cv2.calcHist([image], [0,1,2], None, [256, 256, 256], [0, 256, 0,256, 0, 256])

test1 = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/traffic/traffic001.png"
test2 = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/traffic/traffic002.png"
test3 = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/first001.png"
img1 = cv2.imread(test1)
img2 = cv2.imread(test2)
img3 = cv2.imread(test3)
hist1 = cv2.calcHist([img1], [0,1,2], None, [256, 256, 256], [0, 256, 0,256, 0, 256])
hist2 = cv2.calcHist([img2], [0,1,2], None, [256, 256, 256], [0, 256, 0,256, 0, 256])
hist3 = cv2.calcHist([img3], [0,1,2], None, [256, 256, 256], [0, 256, 0,256, 0, 256])
d = cv2.compareHist(hist1, hist2, 4)
d2 = cv2.compareHist(hist1, hist1, 4)
d3 = cv2.compareHist(hist1, hist3, 4)
print(d)
print(d2)
print(d3)

