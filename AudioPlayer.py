#coding=utf-8


import pyaudio
import wave
from PIL import Image, ImageQt


def imgRead(loc):
    in_file = open("/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/"+loc, "rb") # opening for [r]eading as [b]inary
    data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
    # print(data.__len__())
    img = Image.new('RGB',(352,288),'white')
    # img.show()
    pixels = img.load()
    # pixels[351,100]=(1,177,177)
    # img.show()
    lim =data.__len__()
    # print(data)
    ba = []
    pos = 0
    while(pos<lim):
        in_file.seek(pos)
        ba.append(int.from_bytes(in_file.read(1), byteorder='big'))
        # print(ba[pos])
        pos+=1
    ind =0
    for y in range(0,288):
        for x in range(0,352):
            pixels[x, y] = (ba[ind],ba[ind+(288*352)],ba[ind+(288*352*2)])
            ind+=1
    # print(pos)
    # print(ind)
    # for y in range(0,288):
    #     for x in range(0,352):
    #         print("%s %s"%(pixels[x,y],(y+1)))
    #         ind+1
    in_file.close()
    # return img
    img.show()

#define stream chunk
chunk = 1024

#open a wav format music
f = wave.open("/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/first.wav", "rb")
print(f.getnframes())
print("Frame Rate: ", f.getframerate())



#instantiate PyAudio
p = pyaudio.PyAudio()
#open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data
data = f.readframes(chunk)
print(data.__len__())
fileName = "first"
fileExt = ".rgb"
fileNum = ["001", "032", "063", "080", "115", "150"]
index = 0
loopCount = 0

#play stream

while data:
    stream.write(data)
    data = f.readframes(chunk)
    if ((loopCount % 36) == 0):
        index+=1
        imgRead(fileName + fileNum[index] + fileExt)
    loopCount += 1

print(loopCount)
#stop stream
stream.stop_stream()
stream.close()

#close PyAudio
p.terminate()