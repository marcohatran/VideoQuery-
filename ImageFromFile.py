import os
from PIL import ImageTk, Image
from ImageReader import imgRead
from tkinter import Tk, Frame, Label, PhotoImage, Button
import time

root = Tk()
# frame = Frame(root)
root.title("Media Player")
root.minsize(width=500, height = 500)
count=0
c=0
loc = '/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first'

def QLocSet(dirAddress):
    global loc
    loc = dirAddress

Images = [] #list of image filenames
dirFiles = os.listdir(loc) #list of directory files
dirFiles.sort()

def fillImageArr():
    global count
    for files in dirFiles:  # filter out all non jpgs
        # print(files.title())
        if '.rgb' in files:
            Images.append(ImageTk.PhotoImage(imgRead(files.title())))
            count += 1
    #might want to take a return statement on the number of count to determine how many frames to display per audio packet

def showLabel1(c):
    # global count
    # while (c<count):
    labelref = Label(root, image=Images[0])
    return labelref
        # c+=1
        # label1.after(4000, showLabel1)
    # label1.destroy()
    # print("reached")
    # canvas.create_image(100, 80, image=Images[num])
    # print(num)
    # canvas.pack()

fillImageArr()
label1 = Label(root, image=Images[0]) #blank label
label1.place(x=20,y=20)
print("fames are to be displayed soon")

def callback(e):
    global c
    global count
    if c>count:
        c=0
    # print("counter methed %s",c)
    PlayLabel = Label(root, image=Images[c])
    PlayLabel.place(x=20,y=20)
    c+= 1
    # PlayLabel.pack()
# # # print("reached end")
# #     root.bind()
root.bind("<Return>", callback)
root.mainloop()
# print("end")
         # self.ImageSequencer()
# self.ImageSequencer()

# # print(tifCounter)
#
#   ###maybe add a return flag here to say all the images are obtained and play can be considered functional after this
# #     elif '.wav' in files:
# #         audio = files
# # print len(images)
# # print images
# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 button - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 320
#         self.height = 200
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         self.show()
#         self.convertRgbtoImgArr()
#
#     def ConvertRgbtoImgArr(self):
#
#         count = 0
#         for files in dirFiles:  # filter out all non jpgs
#             #     # print(files.title())
#             if '.rgb' in files:
#                 Images[count] = imgRead(files.title())  # this isnt matching data type
#                 count += 1
#         self.ImageSequencer()
#
#     def ImageSequencer(self):
#         timeLine = QTimeLine(1500, self)
#         timeLine.setFrameRange(self, 0, Images.__len__())
#         timeLine.start(self)
#         timeLine.frameChanged[int].connect(frameChanged(int))    #t(timeLine, SIGNAL(frameChanged(int)), progressBar, SLOT(setValue(int)));
#
#     def frameChanged(self, x):
#
#     @pyqtSlot()
#     def on_click(self):
#         print('PyQt5 button click')
#
#
# # if __name__ == '__main__':
# app = QApplication(sys.argv)
# ex = App()
# sys.exit(app.exec_())
#
#
# # ConvertRgbtoImgArr()
# # App()
# timeLine = QtCore.QTimeLine()
# QtCore.QTimeLine.setFrameRange(timeLine,StartFrame,150)

#
#
# mineImagesList = [PhotoImage(file="Resources/Mine/saperx_mine_%s.png" % (frame)) for frame in range(1, 11)]
# button = Button(root, bd=0, relief=FLAT, command= lambda: func(button))
#
#
# def func (object, frame=0):
#     object.configure(image=mineImagesList[frame])
#     object.image = mineImagesList[frame]
#     print("Object image:", object.image)
#     if frame+1 < len(mineImagesList):
#         frame += 1
#         root.after(34, lambda frame=frame, object=object: func(object=object, frame=frame))
#
# button.pack()
# root.mainloop()
