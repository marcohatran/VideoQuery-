from ImageReader import imgRead
import os
import subprocess

class MakeAviData:

    Dir_Paths = ["/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/",
                      "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/"]

    def __init__(self):
        self.MakeAllPngs()

    def MakePngFromRgb(self, dir_path):
        dirFiles = os.listdir(dir_path) #list of directory files
        dirFiles.sort()
        count =0
        images = []
        for f in dirFiles:
            if '.rgb' in f:
                images.append(imgRead(dir_path+f.title()))
                images[count].save(dir_path+f.title()[:-3].lower()+'png',"PNG")
                count += 1
        self.MakeAviFromPng(dir_path)

    def MakeAllPngs(self):
        for file_paths in self.Dir_Paths:
            for folders in os.listdir(file_paths):
                collection_files = file_paths+folders.title().lower()+'/'
                if os.path.isdir(collection_files):
                    png_found = False
                    for tiles in os.listdir(collection_files):
                        if '.png' in tiles:
                            png_found = True
                    if png_found is False:
                        self.MakePngFromRgb(collection_files)

    def MakeAviFromPng(self, dir_path):
        basic_name = os.path.basename(os.path.dirname(dir_path))
        img_name = dir_path+basic_name
        wav_name = dir_path+basic_name+'.wav'
        avi_name = dir_path+basic_name+'.avi'
        subprocess.call(['ffmpeg', '-framerate', '30',
                         '-i', img_name+'%03d.png',
                         '-i', wav_name,
                         avi_name])


prep = MakeAviData()
