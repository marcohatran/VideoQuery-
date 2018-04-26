import cv2
import os
import csv

class MakeHistData:

    Dir_Paths = ["/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/"]
                      #"/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/"]

    def __init__(self):
        self.GetAllHists()

    def MakeCsvFromPng(self, dir_path, data_file):
        file_writer = csv.writer(open(data_file,'a'), delimiter = ',', quoting = csv.QUOTE_ALL)
        dirFiles = os.listdir(dir_path) #list of directory files
        dirFiles.sort()
        for f in dirFiles:
            if '.png' in f:
                img_add = dir_path+f.title().lower()
                ImgtoHist = cv2.imread(img_add)
                histb = cv2.calcHist([ImgtoHist], [0], None, [256], [0, 256])
                histg = cv2.calcHist([ImgtoHist], [1], None, [256], [0, 256])
                histr = cv2.calcHist([ImgtoHist], [2], None, [256], [0, 256])
                frame_number = f.title()[-7:-4]
                for i in range(0,256):
                    file_writer.writerow([frame_number,float(histb[i]),float(histg[i]),float(histr[i])])

    def GetAllHists(self):
        for file_paths in self.Dir_Paths:
            for folders in os.listdir(file_paths):
                collection_files = file_paths+folders.title().lower()+'/'
                if os.path.isdir(collection_files):
                    csv_found = False
                    for tiles in os.listdir(collection_files):
                        if '.csv' in tiles:
                            csv_found = True
                    if csv_found is False:
                        csv_filename = collection_files+os.path.basename(os.path.dirname(collection_files))+'Hist.csv'
                        print("making csv in" +csv_filename)
                        with open(csv_filename, 'a') as HistDatabase:
                            file_writer = csv.writer(HistDatabase, delimiter = ',', quoting = csv.QUOTE_ALL)
                            file_writer.writerow(['image_number','blue_histogram','green_histogram','red_histogram'])
                        self.MakeCsvFromPng(collection_files, csv_filename)


prep = MakeHistData()