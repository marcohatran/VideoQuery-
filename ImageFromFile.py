import os
from PIL import ImageTk
from ImageReader import imgRead
import glob
import tkinter as tk

root = tk.Tk()
root.title("Media Player")
label1 = tk.Label(root)
count=0
c=0
Images = [] #list of image filenames
dirFiles = os.listdir('/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first') #list of directory files
dirFiles.sort()

def fillImageArr():
    global count
    for files in dirFiles:  # filter out all non jpgs
        # print(files.title())
        if '.rgb' in files:
            Images.append(ImageTk.PhotoImage(imgRead(files.title())))
            count += 1

def showLabel1(label1):
    def showLabel():
        global c
        global count
        if c!=count:
            label1.config(image = Images[c])
            label1.image = Images[c]
            label1.after(4000, showLabel1)
        else:
            label1.destroy()
    showLabel()
    # print("reached")
    # canvas.create_image(100, 80, image=Images[num])
    # print(num)
    # canvas.pack()

fillImageArr()
print("fames are to be displayed soon")
label1.pack()
showLabel1(label1)
root.mainloop()
print("end")
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
