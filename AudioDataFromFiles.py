import librosa
import numpy as np
import csv
import os

class AudioFromFiles:
    Dir_Paths = ["/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/query/",
                 "/Users/taufeqrazakh/Documents/school/CSCI_576/Project_CSCI_567/databse_videos/"]

    def __init__(self):
        self.GetFullAudioArray()

    def GetFullAudioArray(self):
        for file_paths in self.Dir_Paths:
            for folders in os.listdir(file_paths):
                collection_files = file_paths+folders.title().lower()+'/'
                if os.path.isdir(collection_files):
                    csv_found = False
                    for tiles in os.listdir(collection_files):
                        if 'AudioArray.csv' in tiles:
                            csv_found = True
                    if csv_found is False:
                        csv_filename = collection_files+os.path.basename(os.path.dirname(collection_files))+'AudioArray.csv'
                        print("making csv in " +csv_filename)
                        with open(csv_filename, 'a') as MotionvectorsDatabase:
                            file_writer = csv.writer(MotionvectorsDatabase, delimiter = ',', quoting = csv.QUOTE_ALL)
                            file_writer.writerow(['audio data'])
                        self.MakeAudioArray(collection_files, csv_filename)

    def MakeAudioArray(self, dir_path, data_file):
        file_writer = csv.writer(open(data_file,'a'), delimiter = ',', quoting = csv.QUOTE_ALL)
        basic_name = os.path.basename(os.path.dirname(dir_path))
        wav_name = dir_path + basic_name + '.wav'
        y, sr = librosa.load(wav_name)
        for i in range(0,np.size(y)):
            file_writer.writerow([y[i]])

prep = AudioFromFiles()