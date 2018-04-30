from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import cv2
import csv

DatabaseAd = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/"
QueryAd = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/"

query_ad = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/second/secondHist.csv"
database_ad = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/sports"

img_ref = cv2.imread("/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/second/second002.png")
rarray = np.empty((256,1))
garray = np.empty((256,1))
barray = cv2.calcHist([img_ref], [1], None, [256], [0,256])
print(np.shape(barray))
barray2 = np.empty((256,1), float)
arr1 = np.empty([])

bhist_ref = cv2.calcHist([img_ref], [0], None, [256], [0,256])
rhist_ref = cv2.calcHist([img_ref], [1], None, [256], [0,256])
ghist_ref = cv2.calcHist([img_ref], [2], None, [256], [0,256])
hist_ref = cv2.calcHist([img_ref], [0,1,2], None, [256,256,256], [0,256,0,256,0,256])
print(np.size(hist_ref))
print(np.shape(hist_ref))
# print(barray)
# print(hist_ref)
with open(query_ad, 'r') as csv_hist_data:
    reader = csv.reader(csv_hist_data)
    header = next(reader)
    elements =  [dank_lines for dank_lines in reader]
    max = -999
    initi=0
    print("printing the array from csv\n")
    for values in range(0,256):
        # rarray = np.append((rarray , np.array(elements[values][1])))
        barray[values] = np.array([[float(elements[values][1])]])
        garray = np.append(garray, np.array([elements[values][3]]))
        arr1=np.append(arr1, np.array([[elements[values][1],elements[values][2],elements[values][3]]]))
        initi = elements[0]
        max = elements[values]
    # print(arr1)
    # print(max)
    # print(initi)
    # np.reshape(arr1,(256,256,256))
    # print(cv2.compareHist(hist_ref,hist_ref,1))

    for values in range (256, (256*2)):
        barray2[values-256] = np.array([[float(elements[values][1])]])
    #     initi = elements[256]
    #     max = elements[values]
    # print(np.size(barray), np.shape(barray))
    print(barray)

    print("corresponding histogram\n")
    #
    print(bhist_ref)

    np.reshape(barray, (256,1))
    np.reshape(barray2, (256,1))
    # print(np.correlate(barray, barray2))
    c1 = cv2.compareHist(bhist_ref, barray, cv2.HISTCMP_CORREL)
    # c2 = cv2.compareHist(rarray, rhist_ref, 1)
    # c3 = cv2.compareHist(garray, ghist_ref, 1)
    # c =c1+c2+c3/3
    print(c1)
    # print(max)
    # print(initi)
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


# hist0 = np.empty((256,256,256))
# for folders in os.listdir(DatabaseAd+'traffic/'):
#     if '.png' in folders:
#         image = cv2.imread(DatabaseAd+'traffic/'+folders.title().lower())
#         hist0 = cv2.calcHist([image], [0,1,2], None, [256, 256, 256], [0, 256, 0,256, 0, 256])
#
# test1 = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/traffic/traffic001.png"
# test2 = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/traffic/traffic002.png"
# test3 = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/first001.png"
# img1 = cv2.imread(test1)
# img2 = cv2.imread(test2)
# img3 = cv2.imread(test3)
# histr = cv2.calcHist([img1], [0], None, [256], [0,256])
# histg = cv2.calcHist([img1], [1], None, [256], [0,256])
# histb = cv2.calcHist([img1], [2], None, [256], [0,256])
# imageNum = 53
# dir = 2
# for i in range (0,255):
#     newStr = dir,imageNum,int(histr[i]),int(histg[i]),int(histg[i])
#     print (newStr)
#




#for i in range (0,2):
#     histr = cv2.calcHist([img1], [i], None, [256], [0, 256])
#     np.save("firstr", histr, delimiter)
# hist1 = cv2.calcHist([img1], [0,1,2], None, [256,256,256], [0,256,0,256,0,256])
# hist2 = cv2.calcHist([img2], [0,1,2], None, [256, 256, 256], [0, 256, 0,256, 0, 256])
# hist3 = cv2.calcHist([img3], [0,1,2], None, [256, 256, 256], [0, 256, 0,256, 0, 256])

#print(hist1)
# with open(DatabaseAd+'database_metrics', 'a') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter = ',',
#                             quotechar = '|', quoting = csv.QUOTE_MINIMAL)
#     filewriter.writerow(['check','check'])
#     filewriter.writerow([test1, hist1])

# d = cv2.compareHist(hist1, hist2, 4)
# d2 = cv2.compareHist(hist1, hist1, 4)
# # d3 = cv2.compareHist(hist1, hist3, 4)
# print(d)
# print(d2)
# print(d3)

