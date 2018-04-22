#!/usr/local/bin/python3
from PIL import ImageTk
import cv2
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
                collection_files = file_paths+folders.title()+'/'
                if os.path.isdir(collection_files):
                    png_found = False
                    for tiles in os.listdir(collection_files):
                        if '.png' in tiles:
                            png_found = True
                    if png_found is False:
                        self.MakePngFromRgb(collection_files)

    def MakeAviFromPng(self, dir_path):
        basic_name = os.path.basename(dir_path)
        img_name = dir_path+basic_name
        wav_name = dir_path+basic_name+'.wav'
        avi_name = dir_path+basic_name+'.avi'
        subprocess.call(['ffmpeg',
                         '-framerate', '30',
                         '-i', img_name+'03%d.png',
                         '-i', wav_name,
                         avi_name])


prep = MakeAviData()

# # Determine the width and height from the first image
# image_path = os.path.join(dir_path, images[0])
# frame = cv2.imread(image_path)
# cv2.imshow('video',frame)
# height, width = 288, 352
#
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'MJPG') # Be sure to use lower case
# out = cv2.VideoWriter("flvref.avi", fourcc, 30.0, (width, height))
#
# for image in images:
#
#     image_path = os.path.join(dir_path, image)
#     frame = cv2.imread(image_path)
#
#     out.write(frame) # Write out frame to video
#
#     cv2.imshow('video',frame)
#     if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
#         break
#
# # Release everything if job is finished
# out.release()
# cv2.destroyAllWindows()
#
# print("The output video is {}".format(output))
