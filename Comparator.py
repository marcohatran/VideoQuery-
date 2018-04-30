import numpy as np
import cv2
import csv
import os
import scipy.spatial.distance


class ExtractAllMetrics:
    # made a default address here.
    # change the address of this variable with selection from media player interface

    Query_path = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/second/"
    # change database location here
    Database_path = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/"

    img_ref = cv2.imread('sample.png')
    ref_array = cv2.calcHist([img_ref], [0], None, [256], [0,256])
    Q_B_Array = np.empty((150,256,1))
    Q_G_Array = np.empty((150,256,1))
    Q_R_Array = np.empty((150,256,1))

    D_B_Array = np.empty((600,256,1))
    D_G_Array = np.empty((600,256,1))
    D_R_Array = np.empty((600,256,1))

    # Q_R = np.empty((256,1))
    # Q_G = np.empty((256,1))
    # Q_B = np.empty((256,1))
    #
    # D_R = np.empty((256,1))
    # D_G = np.empty((256,1))
    # D_B = np.empty((256,1))

    for i in range (0,600):
        D_B_Array[i] = ref_array
        D_G_Array[i] = ref_array
        D_R_Array[i] = ref_array
        D_B = ref_array
        D_G = ref_array
        D_R = ref_array
        if i<150:
            Q_B_Array[i] = ref_array
            Q_G_Array[i] = ref_array
            Q_R_Array[i] = ref_array
            Q_B = ref_array
            Q_G = ref_array
            Q_R = ref_array
    # print(ref_array, np.count_nonzero(ref_array))
    # print(Q_B_Array[0], np.size(Q_B_Array[0]),np.count_nonzero(Q_B_Array[0]))
    Image_Correlations = ["/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/flowers/",
                          "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/interview/",
                          "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/movie/",
                          "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/musicvideo/",
                          "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/sports/",
                          "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/starcraft/",
                          "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/traffic/"]

    correlation = 0
    start_index = 0
    # print(Image_Correlations[0][0])

    def __init__(self):
        print('starting a pyclass')
        self.q_extract_hist(self.Query_path)
        self.compare_hist()
        # print(self.Q_B_Array, self.Q_B, self.D_B_Array, self.D_B)

    def q_extract_hist(self, Q_dir_path):
        print(Q_dir_path)
        # extracting histogram data from all queries
        for file in os.listdir(Q_dir_path):
            if 'Hist.csv' in file:
                data_file_loc = Q_dir_path+file.title().lower()
                with open(data_file_loc, 'r') as csv_hist_data:
                    reader1 = csv.reader(csv_hist_data)
                    header = next(reader1)
                    elements = [lines for lines in reader1]
                    count = 0
                    track = 0
                    bin=0
                    # print(np.size(elements), np.shape(elements)[0])
                    for values in range (0,np.shape(elements)[0]):
                        # print(i,rest)
                        self.Q_B_Array[count][bin] = np.array([[float(elements[values][1])]])
                        self.Q_G_Array[count][bin] = np.array([[float(elements[values][2])]])
                        self.Q_R_Array[count][bin] = np.array([[float(elements[values][3])]])
                        track+=1
                        bin+=1
                        # zero index corresponds to image 1
                        if (track % 256 == 0):
                            count += 1
                            bin = 0
        # print('from query B',self.Q_B_Array[0])

    def load_hist(self, D_dir_path):
        print(D_dir_path)
        for tiles in os.listdir(D_dir_path):
            if 'Hist.csv' in tiles:
                data_file_loc = D_dir_path + tiles.title().lower()
                with open(data_file_loc, 'r') as csv_hist_data:
                    reader2 = csv.reader(csv_hist_data)
                    header = next(reader2)
                    elements = [lines for lines in reader2]
                    count = 0
                    track = 0
                    bin = 0
                    for values in range(0, np.shape(elements)[0]):
                        self.D_B_Array[count][bin] = np.array([[float(elements[values][1])]])
                        self.D_G_Array[count][bin] = np.array([[float(elements[values][2])]])
                        self.D_R_Array[count][bin] = np.array([[float(elements[values][3])]])
                        track += 1
                        bin += 1
                        # zero index corresponds to image 1
                        if track % 256 == 0:
                            count += 1
                            bin = 0
        # print('from datababse B',self.D_B_Array[0])


    def transformations(self, index, shift):
        for j in range(0, 256):
            self.Q_B[j] = self.Q_B_Array[index][j][0]
            print(self.Q_B_Array[index][j][0])
            self.Q_G[j] = self.Q_G_Array[index][j][0]
            self.Q_R[j] = self.Q_R_Array[index][j][0]
            self.D_B[j] = self.D_B_Array[index + shift][j][0]
            self.D_G[j] = self.D_G_Array[index + shift][j][0]
            self.D_R[j] = self.D_R_Array[index + shift][j][0]
        print('from transform Q',self.Q_B,'\n','input has to be same as query B', self.Q_B_Array)
        # print(self.D_B, self.D_B_Array)


    def compare_hist(self):
        # print(np.shape(Q_B_Array))
        for (line, address) in enumerate(self.Image_Correlations):
            self.load_hist(address)
            # print(D_B_Array,'\n',ref_array)
            for offset in range (0, 450, 20):
                cumulative_correlation = 0.000
                for i in range (0,150):
                    self.transformations(i, offset)
                    # print(self.Q_B, self.Q_B_Array)
                    # print(self.D_B, self.D_B_Array)
                    c1 = cv2.compareHist(self.Q_B, self.D_B, cv2.HISTCMP_CORREL)
                    c2 = cv2.compareHist(self.Q_G, self.D_G, cv2.HISTCMP_CORREL)
                    c3 = cv2.compareHist(self.Q_R, self.D_R, cv2.HISTCMP_CORREL)
                    c = float((c1+c2+c3)/3)
                    cumulative_correlation += c
                    # print(c)
                cumulative_correlation = cumulative_correlation/150
                print(cumulative_correlation)
                # if cumulative_correlation>=correlation:
                #     Image_Correlations[line][1] = cumulative_correlation
                #     Image_Correlations[line][2] = offset

prep = ExtractAllMetrics()