import numpy as np
import cv2
import csv
import os
import scipy.spatial.distance
import scipy.stats
import librosa

class ExtractAllMetrics:
    # made a default address here.
    # change the address of this variable with selection from media player interface

    Query_path = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/Q4/"
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

    Q_A_Array = []
    D_A_Array = []

    Q_M_Array = []
    D_M_Array = []
    min = 999
    which  = ''
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
        # self.q_extract_hist(self.Query_path)
        # self.compare_hist()
        # self.q_extract_audio(self.Query_path)
        # self.compare_audio()
        # print(self.min)
        self.q_extract_motionvectors(self.Query_path)
        self.compare_motionvectors()
        print(self.min)
        print(self.which)
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

    def compare_hist(self):
        # print(np.shape(Q_B_Array))
        for (line, address) in enumerate(self.Image_Correlations):
            self.load_hist(address)
            # print(D_B_Array,'\n',ref_array)
            for offset in range (0, 450, 2):
                cumulative_correlation = 0.000
                for i in range (0,150):
                    # self.transformations(i, offset)
                    # print(self.Q_B, self.Q_B_Array)
                    # print(self.D_B, self.D_B_Array)
                    c1 = scipy.stats.pearsonr(np.ndarray.flatten(self.Q_B_Array[i]), np.ndarray.flatten(self.D_B_Array[i+offset]))
                    c2 = scipy.stats.pearsonr(np.ndarray.flatten(self.Q_G_Array[i]), np.ndarray.flatten(self.D_G_Array[i+offset]))
                    c3 = scipy.stats.pearsonr(np.ndarray.flatten(self.Q_R_Array[i]), np.ndarray.flatten(self.D_R_Array[i+offset]))
                    c = float((c1[0]+c2[0]+c3[0])/3)
                    cumulative_correlation += c
                    # print(c)
                cumulative_correlation = cumulative_correlation/150
                print(cumulative_correlation)
                # if cumulative_correlation>=correlation:
                #     Image_Correlations[line][1] = cumulative_correlation
                #     Image_Correlations[line][2] = offset


    def q_extract_audio(self, Q_dir_path):
        print(Q_dir_path)
        # extracting audio data from given queries
        for file in os.listdir(Q_dir_path):
            if 'AudioArray.csv' in file:
                data_file_loc = Q_dir_path + file.title().lower()
                with open(data_file_loc, 'r') as csv_hist_data:
                    reader1 = csv.reader(csv_hist_data)
                    header = next(reader1)
                    elements = [lines for lines in reader1]
                    # print(elements[0],np.shape(elements),elements[0][0])
                    track = 0
                    # print(np.size(elements), np.shape(elements)[0])
                    for values in range(0, np.shape(elements)[0]):
                        # print(i,rest)
                        # print(float(elements[values][0]))
                        self.Q_A_Array.append(float(elements[values][0]))
                        track += 1
                    # print(self.Q_A_Array, track)


    def load_audio(self, D_dir_path):
        print(D_dir_path)
        for tiles in os.listdir(D_dir_path):
            if 'AudioArray.csv' in tiles:
                data_file_loc = D_dir_path + tiles.title().lower()
                with open(data_file_loc, 'r') as csv_hist_data:
                    reader2 = csv.reader(csv_hist_data)
                    header = next(reader2)
                    elements = [lines for lines in reader2]
                    track = 0
                    for values in range(0, np.shape(elements)[0]):
                        self.D_A_Array.append(float(elements[values][0]))
                        track += 1
                        # zero index corresponds to image 1
                    # print(self.D_A_Array, track)


    def compare_audio(self):
        for (line, address) in enumerate(self.Image_Correlations):
            self.D_A_Array = []
            self.load_audio(address)
            for offset in range(0, (self.D_A_Array.__len__()-self.Q_A_Array.__len__()), 20000):
                # print(self.D_A_Array.__len__()-self.Q_A_Array.__len__())
                db_audio_array =[]
                for i in range(0, self.Q_A_Array.__len__()):
                    db_audio_array.append(self.D_A_Array[offset+i])
                # print(db_audio_array.__len__())
                load1 = np.asarray(self.Q_A_Array)
                np.resize(load1,(load1.__len__(),1))
                load2 = np.asarray(db_audio_array)
                np.resize(load2, (load2.__len__(), 1))
                chroma1 = librosa.feature.rmse(y=load1)
                chroma2 = librosa.feature.rmse(y=load2)
                # print(np.size(chroma2),np.size(chroma1))
                # print(chroma1,chroma2)
                # c = scipy.stats.pearsonr(np.array(self.Q_A_Array), np.array(db_audio_array))
                c = scipy.spatial.distance.euclidean(chroma1,chroma2)
                cumulative_correlation = c
                print(cumulative_correlation)
                if self.min>cumulative_correlation:
                    self.min = cumulative_correlation


    def q_extract_motionvectors(self, Q_dir_path):
        print(Q_dir_path)
        # extracting audio data from given queries
        for file in os.listdir(Q_dir_path):
            if 'MotionVectors.csv' in file:
                data_file_loc = Q_dir_path + file.title().lower()
                with open(data_file_loc, 'r') as csv_hist_data:
                    reader1 = csv.reader(csv_hist_data)
                    header = next(reader1)
                    elements = [lines for lines in reader1]
                    # print(elements[0],np.shape(elements),elements[0][0])
                    track = 0
                    # print(np.size(elements), np.shape(elements)[0])
                    for values in range(0, np.shape(elements)[0]):
                        self.Q_M_Array.append(float(elements[values][0]))
                        track += 1
                    # print(self.Q_M_Array, track)

    def load_motionvectors(self, D_dir_path):
        print(D_dir_path)
        for tiles in os.listdir(D_dir_path):
            if 'MotionVectors.csv' in tiles:
                data_file_loc = D_dir_path + tiles.title().lower()
                with open(data_file_loc, 'r') as csv_hist_data:
                    reader2 = csv.reader(csv_hist_data)
                    header = next(reader2)
                    elements = [lines for lines in reader2]
                    track = 0
                    for values in range(0, np.shape(elements)[0]):
                        self.D_M_Array.append(float(elements[values][0]))
                        track += 1
                        # zero index corresponds to image 1
                    # print(self.D_A_Array, track)


    def compare_motionvectors(self):
        for (line, address) in enumerate(self.Image_Correlations):
            self.D_M_Array = []
            self.load_motionvectors(address)
            for offset in range(0, self.D_M_Array.__len__()-self.Q_M_Array.__len__(), 5):
                cumulative_correlation = 0.000
                # print(self.D_A_Array.__len__()-self.Q_A_Array.__len__())
                db_motion_vector =[]
                for i in range(0, self.Q_M_Array.__len__()):
                    db_motion_vector.append(self.D_M_Array[offset+i])
                # print(db_audio_array)
                c = scipy.spatial.distance.euclidean(np.array(self.Q_M_Array), np.array(db_motion_vector))
                cumulative_correlation = c
                print(cumulative_correlation)
                if self.min>cumulative_correlation:
                    self.min = cumulative_correlation
                    self.which = address
prep = ExtractAllMetrics()