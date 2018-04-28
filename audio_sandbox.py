
import librosa
from librosa import display
import numpy as np
import scipy.spatial.distance
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import pyaudio
import wave

# set desired values
start = 7
length = 3

# open wave file
f1 ="/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/query/first/first.wav"
f2 = "/Users/taufeqrazakh/Documents/school/CSCI 576/Project_CSCI_567/databse_videos/musicvideo/musicvideo.wav"
f1audio = wave.open(f1,'rb')
# print(f1audio.getnframes())
# a = read(f1)
# b = read(f2)
# np.array(a[1],dtype=float)
# print((np.size(a[1])))

y1, sr1 = librosa.load(f1)
print(np.size(y1),np.shape(y1))
chroma1 = librosa.feature.rmse(y=y1)
print(chroma1)
# print(np.size(chroma1), np.shape(chroma1))
f2audio = wave.open(f2,'rb')
# print(f2audio.getnframes())
y2, sr2 = librosa.load(f2)
print(np.size(y2))
load = np.empty((110592,))
load2 = np.empty((110592,))
for i in range(0,110592):
    load[i]=y2[i]
for i in range(110592, 221184):
    load2[i-110592] = y2[i]
chromacomp = librosa.feature.rmse(y=load)
print(chromacomp)
chromacomp2 = librosa.feature.rmse(y=load2)
final = scipy.spatial.distance.euclidean(chromacomp, chroma1)
final2 = scipy.spatial.distance.euclidean(chromacomp2, chroma1)
print(np.shape(chromacomp),np.shape(chroma1))
print(final,final2)

# np.ndarray.flatten()

plt.figure(figsize=(10, 4))
# librosa.display.specshow(chroma1, y_axis='chroma', x_axis='time')
# plt.colorbar()
# plt.title('Chromagram')
# plt.tight_layout()
# for values in range():

#
# initialize audio
# py_audio = pyaudio.PyAudio()
# stream = py_audio.open(format=py_audio.get_format_from_width(wave.getsampwidth()),
#                        channels=wave.getnchannels(),
#                        rate=wave.getframerate(),
#                        output=True)
#
# # skip unwanted frames
# n_frames = int(start * wave.getframerate())
# wave.setpos(n_frames)
#
# # write desired frames to audio buffer
# n_frames = int(length * wave.getframerate())
# frames = wave.readframes(n_frames)
# stream.write(frames)
#
# # close and terminate everything properly
# wave.close()
# stream.close()
# py_audio.terminate()


# y, sr = librosa.load(f1)
# first_stft = librosa.feature.rmse(y=y, frame_length=f1audio.getnframes())
# y2, sr2 = librosa.load(f2)
# second_stft = librosa.feature.rmse(y=y, frame_length=f2audio.getnframes())
# for line in first_stft:
#     print(line)
# for line in  second_stft:
#     print(line)
# print(np.size(first_stft), np.shape(first_stft))
# print(np.size(second_stft), np.shape(second_stft))