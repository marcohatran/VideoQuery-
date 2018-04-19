import tkinter as tk
import pyaudio
import wave
import os
from PIL import ImageTk, Image
from ImageReader import imgRead

class Example(tk.Frame):
    playBool = False
    query = "first/first.wav"
    # Set vid params
    count = 0
    c = 0
    loc = "/Users/baltz/Desktop/project_576/query/first"
    Images = []  # list of image filenames
    dirFiles = os.listdir(loc)  # list of directory files
    dirFiles.sort()



    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # set default media player size
        root.geometry('900x700')
        root.title("Media Player")

        # Set vid params
        self.fillImageArr()
        self.label1 = tk.Label(root, image=self.Images[0])  # blank label
        self.label1.place(x=20, y=20)
        print("fames are to be displayed soon")

        # Create menu for tk frame
        menu = tk.Menu(parent)
        parent.config(menu=menu)
        filemenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="First", command=self.first)
        filemenu.add_command(label="Second", command=self.second)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        #self.prompt = tk.Label(self, text="Enter a number:", anchor="w")
        #self.entry = tk.Entry(self)
        self.play = tk.Button(self, text="Play", command = self.playPause)
        #self.submitL = tk.Button(self, text="Pause", command=self.pause)
        self.output = tk.Label(self, text="Paused")

        # lay the widgets out on the screen.
        #self.prompt.pack(side="top", fill="x")
        #self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.play.pack(side="bottom")
        #self.submitL.pack(side="left")


    def playPause(self):
        Example.playBool = not Example.playBool
        if Example.playBool:
            self.output.configure(text = "Playing")
            self.play.configure(text = "Pause")
            self.playAduio()
        else:
            self.output.configure(text = "Paused")
            self.play.configure(text = "Play")

    def playAduio(self):
        # define stream chunk
        chunk = 1024

        # open a wav format music
        f = wave.open("/Users/baltz/Desktop/project_576/query/" + Example.query, "rb")
        print(f.getnframes())
        print("Frame Rate: ", f.getframerate())

        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)
        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

            #update video
            self.callback

        # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()

        # reset Media Player
        self.play.configure(text="Play")
        self.output.configure(text="Paused")
        Example.playBool = False

    def first(self):
        Example.query = "first/first.wav"

    def second(self):
        Example.query = "second/second.wav"

    def fillImageArr(self):
        global count
        for files in self.dirFiles:  # filter out all non jpgs
            # print(files.title())
            if '.rgb' in files:
                self.Images.append(ImageTk.PhotoImage(imgRead(files.title())))
                self.count += 1
        # might want to take a return statement on the number of count to determine how many frames to display per audio packet


    def callback(self):
        global c
        global count
        global label1
        if c == count:
            c = 0
        # print("counter methed %s",c)
        self.label1.destroy()
        self.label1 = tk.Label(root, image=tk.Images[c])
        self.label1.place(x=20, y=20)
        c += 1



    def calculate(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:
            i = int(self.entry.get())
            result = "%s*2=%s" % (i, i*2)
        except ValueError:
            result = "Please enter digits only"

        # set the output widget to have our result
        self.output.configure(text=result)


# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()