from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import cv2

DatabaseAd = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/"
QueryAd = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/"

for f in os.listdir(DatabaseAd):
    folder_name = DatabaseAd+f.title()
    print(folder_name)
    if os.path.isdir(folder_name):
        for pngFiles in os.listdir(folder_name):
            if '.png' in pngFiles:
                image = cv2.imshow('showoff',pngFiles)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


