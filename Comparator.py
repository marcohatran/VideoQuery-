import numpy as np
import cv2
import csv
import os
import scipy.spatial.distance
import scipy.stats
import librosa
import sys
import matplotlib.pyplot as plt
import time
from scipy.interpolate import spline


class ExtractAllMetrics:
    # made a default address here.
    # change the address of this variable with selection from media player interface

    Query_path = "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/query/first/"



    # print(sys.argv)

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
    Q_M2_Array = []
    D_M2_Array = []

    min = -999
    which  = ''
    # print(ref_array, np.count_nonzero(ref_array))
    # print(Q_B_Array[0], np.size(Q_B_Array[0]),np.count_nonzero(Q_B_Array[0]))
    Image_Correlations = ["/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/flowers/",
                          "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/interview/",
                          "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/movie/",
                          "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/musicvideo/",
                          "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/sports/",
                          "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/starcraft/",
                          "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/traffic/"]


    hist_correlation = 0
    hist_start_index = 0
    audio_correlation = 0
    audio_start_index = 0
    mv_correlation = 0
    mv_start_index = 0
    # print(Image_Correlations[0][0])
    hist_correlations=[]
    motionvector_correlations = []
    audio_correlations = []
    hist_graph_array = []
    audio_graph_array =[]
    motionvector_graph_array =[]


    def __init__(self):
        self.Query_path = str(sys.argv[1])
        print(self.Query_path)
        print('starting a pyclass')
        self.q_extract_hist(self.Query_path)
        self.compare_hist()
        self.min = 999
        self.q_extract_audio(self.Query_path)
        self.compare_audio()


        self.min = -999
        self.q_extract_motionvectors(self.Query_path)
        self.compare_motionvectors()
        self.print_java_csv()
        # print(self.min)
        # print(self.which)
        # print(self.Q_B_Array, self.Q_B, self.D_B_Array, self.D_B)


        self.plt_graphs()

    def q_extract_hist(self, Q_dir_path):
        # print(Q_dir_path)
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
            local_min = -999
            # print(D_B_Array,'\n',ref_array)
            temp_full_array =[]
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
                # print(cumulative_correlation)
                temp_full_array.append(cumulative_correlation)
                if local_min<cumulative_correlation and cumulative_correlation>=0:
                    local_min = cumulative_correlation
                    # self.which = address
                    if(local_min>self.min):
                        self.hist_start_index = offset
                        self.min = local_min
            self.hist_correlations.append(local_min)
            if(local_min == self.min):
                self.hist_graph_array = temp_full_array
        self.hist_correlation = self.min

    def q_extract_audio(self, Q_dir_path):
        # print(Q_dir_path)
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
            temp_audio_array = []
            self.load_audio(address)
            local_min = 99998
            for offset in range(0, (self.D_A_Array.__len__()-self.Q_A_Array.__len__()), 5000):
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
                c = scipy.spatial.distance.euclidean(chroma1,chroma2)
                cumulative_correlation = c
                temp_audio_array.append(cumulative_correlation)

                if local_min > cumulative_correlation:
                    local_min = cumulative_correlation
                    # self.which = address
            if (local_min < self.min):
                        # self.audio_start_index = offset
                self.min = local_min
                self.audio_graph_array = temp_audio_array
            self.audio_correlations.append(local_min)
            if(self.min == local_min):
                self.audio_graph_array = temp_audio_array
        self.audio_correlation = self.min
        self.normalize_audio()

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
                        self.Q_M2_Array.append(float(elements[values][1]))
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
                        self.D_M2_Array.append(float(elements[values][1]))
                        track += 1
                        # zero index corresponds to image 1
                    # print(self.D_A_Array, track)


    def compare_motionvectors(self):
        for (line, address) in enumerate(self.Image_Correlations):
            self.D_M_Array = []
            self.D_M2_Array = []
            local_mv_min=-999
            self.load_motionvectors(address)
            temp_mv = []
            for offset in range(0, self.D_M_Array.__len__()-self.Q_M_Array.__len__(), 5):
                cumulative_correlation = 0.000
                # print(self.D_A_Array.__len__()-self.Q_A_Array.__len__())
                db_motion_vector =[]
                db_motion_vector2 = []
                for i in range(0, self.Q_M_Array.__len__()):
                    db_motion_vector.append(self.D_M_Array[offset+i])
                    db_motion_vector2.append(self.D_M2_Array[offset+i])
                # print(db_audio_array)
                c = scipy.stats.pearsonr(np.array(self.Q_M_Array), np.array(db_motion_vector))
                c2 = scipy.stats.pearsonr(np.array(self.Q_M2_Array), np.array(db_motion_vector2))
                cumulative_correlation = (  c[0]+c2[0] )/2
                if local_mv_min<cumulative_correlation :
                    local_mv_min = cumulative_correlation
                # print(cumulative_correlation)
                temp_mv.append(cumulative_correlation)
            self.motionvector_correlations.append(local_mv_min)
            if local_mv_min>self.min:
                self.min = local_mv_min
                self.motionvector_graph_array = temp_mv
        mv_correlation = self.min

    def normalize_audio(self):
        tmpMax = max(self.audio_graph_array)
        for value in range (0,self.audio_graph_array.__len__()):
            self.audio_graph_array[value] = 1 - (self.audio_graph_array[value] / tmpMax)


    def print_java_csv(self):
        file_writer_boss = csv.writer(open('results.csv', 'w'), delimiter=',', quoting=csv.QUOTE_MINIMAL)
        file_writer_boss.writerow(["histogram"])
        file_writer_boss.writerow([self.hist_correlation])
        file_writer_boss.writerow([self.hist_start_index])
        file_writer_boss.writerow(["hist_arr"])
        for i in range(0,self.hist_correlations.__len__()):
            file_writer_boss.writerow([self.hist_correlations[i]])
        file_writer_boss.writerow(["aduio"])
        file_writer_boss.writerow([self.audio_correlation])
        file_writer_boss.writerow([self.audio_start_index])
        file_writer_boss.writerow(["aud_arr"])
        for i in range(0, self.audio_correlations.__len__()):
            file_writer_boss.writerow([self.audio_correlations[i]])
        file_writer_boss.writerow(["MotionVector"])
        file_writer_boss.writerow([self.mv_correlation])
        file_writer_boss.writerow(["0"])
        file_writer_boss.writerow(["Mv_arr"])
        for i in range(0, self.motionvector_correlations.__len__()):
            file_writer_boss.writerow([self.motionvector_correlations[i]])
        file_writer_boss.writerow(["hist_graph_arr"])
        for i in range(0,self.hist_graph_array.__len__()):
            file_writer_boss.writerow([self.hist_graph_array[i]])
        file_writer_boss.writerow(["audio_graph_arr"])
        for i in range(0, self.audio_graph_array.__len__()):
            file_writer_boss.writerow([self.audio_graph_array[i]])

    def plt_graphs(self):
        x = []
        number = 0
        for i in range(0, self.hist_graph_array.__len__()):
            x.append(number)
            number = number + 2

        x_aud = []
        for i in range(0, self.audio_graph_array.__len__()):
            x_aud.append(i * round(450/self.audio_graph_array.__len__()))
        print(self.hist_graph_array.__len__())
        print(self.audio_graph_array.__len__())
        print(self.motionvector_graph_array.__len__())


        x_mv = []
        for i in range(0,self.motionvector_graph_array.__len__()):
            x_mv.append(i * 450/self.motionvector_graph_array.__len__())

        plt.plot(x, self.hist_graph_array, label="Historgram", c='b', alpha=0.8)
        plt.plot(x_aud, self.audio_graph_array, label="Audio", c='r', alpha=0.8)
        plt.plot(x_mv, self.motionvector_graph_array, label="Motion Vector", c='g', alpha=0.8)
        plt.xlabel('Frame')
        # naming the y axis
        plt.ylabel('Percent Match')
        # giving a title to my graph
        plt.title('Correlation')
        plt.legend()
        plt.savefig("CorrelationData.png")
        plt.show()

prep = ExtractAllMetrics()