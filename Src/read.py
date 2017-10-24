# import pyttsx
# engine = pyttsx.init()
# engine.say('Good morning.')
# engine.runAndWait()
#
# from gtts import gTTS
# import os
# tts = gTTS(text='Good morning', lang='en')
# tts.save("good.mp3")
# os.system("mpg321 good.mp3")

from gtts import gTTS

# Read package
line = ""


def readEnglish(row):
    f = open("../data/en.txt", encoding="utf8")
    line = f.readline()
    while (line != ""):
        tts = gTTS(text=line, lang='en')
        tts.save("../output/" + str(row) + "_en.mp3")
        line = f.readline()
        row = row + 1


def readDeutsch(row):
    f = open("../data/de.txt", encoding="utf8")
    line = f.readline()
    while (line != ""):
        tts = gTTS(text=line, lang='de')
        tts.save("../output/" + str(row) + "_de.mp3")
        line = f.readline()
        row = row + 1


readEnglish(1)
readDeutsch(1)
