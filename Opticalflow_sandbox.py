import numpy as np
import cv2
import os
import csv
import math

class MotionVectorsFromFiles:

    Dir_Paths = ["/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/query/",
     "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/"]

    def __init__(self):
        self.GetAllMotionVectors()

    def GetAllMotionVectors(self):
        for file_paths in self.Dir_Paths:
            for folders in os.listdir(file_paths):
                collection_files = file_paths+folders.title().lower()+'/'
                if os.path.isdir(collection_files):
                    csv_found = False
                    for tiles in os.listdir(collection_files):
                        if 'MotionVectors.csv' in tiles:
                            csv_found = True
                    if csv_found is False:
                        csv_filename = collection_files+os.path.basename(os.path.dirname(collection_files))+'MotionVectors.csv'
                        print("making csv in" +csv_filename)
                        with open(csv_filename, 'a') as MotionvectorsDatabase:
                            file_writer = csv.writer(MotionvectorsDatabase, delimiter = ',', quoting = csv.QUOTE_ALL)
                            file_writer.writerow(['new a','new b','old c','old d'])
                        self.MakeMotionVectors(collection_files, csv_filename)

    def MakeMotionVectors(self, dir_path, data_file):
        file_writer = csv.writer(open(data_file, 'a'), delimiter=',', quoting=csv.QUOTE_ALL)
        basic_name = os.path.basename(os.path.dirname(dir_path))
        avi_name = dir_path + basic_name + '.avi'
        print(avi_name)
        cap = cv2.VideoCapture(avi_name)
        backup_frame = cv2.VideoCapture('sample.avi')
        # params for ShiTomasi corner detection
        feature_params = dict(maxCorners=100,
                              qualityLevel=0.3,
                              minDistance=7,
                              blockSize=7)
        # Parameters for lucas kanade optical flow
        lk_params = dict(winSize=(15, 15),
                         maxLevel=2,
                         criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
        # Create some random colors
        color = np.random.randint(0, 255, (100, 3))
        # Take first frame and find corners in it
        ret, old_frame = cap.read()
        old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
        # Create a mask image for drawing purposes
        mask = np.zeros_like(old_frame)
        timer = 1
        while (1):
            ret, frame = cap.read()
            if frame is None:
                print('end of frame')
                break
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # calculate optical flow
            if p0 is None:
                print('maybe it started here')
                ret, old_frame = backup_frame.read()
                old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
                p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
            # Select good points
            if p1 is None:
                break
            good_new = p1[st == 1]
            good_old = p0[st == 1]
            # draw the tracks
            for i, (new, old) in enumerate(zip(good_new, good_old)):
                a, b = new.ravel()
                c, d = old.ravel()
                # print(a,c,b,d)
                file_writer.writerow([(a-c),(b-d),math.hypot((a-c),(b-d))])
                # mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
                frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
            img = cv2.add(frame, mask)
            cv2.imshow('frame', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
            # Now update the previous frame and previous points
            old_gray = frame_gray.copy()
            p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
            timer +=1
            print(timer)
        cv2.destroyAllWindows()
        cap.release()

prep = MotionVectorsFromFiles()
