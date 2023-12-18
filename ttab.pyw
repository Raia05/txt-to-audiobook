#GUI
from tkinter import Tk
from tkinter.filedialog import askopenfile

Tk().withdraw()

fileobj = askopenfile(initialdir = "/mnt/c/Users/zezdr/Downloads/audio books")

#covert to mp3

booktxt = fileobj.read()
from gtts import gTTS

audiobook = gTTS(booktxt, lang='en', tld = 'ie')

from pathlib import Path 

title = Path(fileobj.name).stem
audiobook.save("/mnt/c/Users/zezdr/Downloads/audio books/recordings/" + (title+'.mp3'))