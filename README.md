# Text2Speech
This project is aimed at providing audio version of the vocabulary list for learning German [1] using Google's Text to Speech API [2]. Though the program is written for this particular purpose, it can be used with other input files as well.

With these audio files, one can read the vocabulary list and listen to them at the same time, making it easier to learn the words and phrases.

It follows the simple algorithm below:

Load file
read line by line
def loadFile(filepath):
     try:
         f = open(filepath, 'r')
         return f
     except:
         print("cannot open " + filepath)
         return
def splitDeEn(f):
     line = f.readline();
     de, en = line.split(',') # split De and EN entries
     START:
     Read the whole line
     Split the English text from the German text and load to DE and EN
     load tts
     create audio file called line_number_de.pm3 and line_number_en.mp3
     read the German text, tts it and write it to line_number_de.mp3
     read the English text, tts it and write it to line_number_en.mp3
     save and close the files
     Goto START

Links:

[1] www.ocr.org.uk/Images/68532-vocabulary-list-by-topic.pdf

[2] https://developers.google.com/translate/