# Text2Speech
This project is aimed at providing audio version of the vocabulary list for learning German [1] using Google's Text to Speech API [2]. Though the program is written for this particular purpose, it can be used with other input files as well.

With these audio files, one can read the vocabulary list and listen to them at the same time, making it easier to learn the words and phrases.

It follows the simple algorithm below:

Load file <br />
read line by line <br />
def loadFile(filepath): <br /> 
     try:  <br />
         f = open(filepath, 'r') <br /> 
         return f  <br />
     except:  <br />
         print("cannot open " + filepath) <br /> 
         return  <br />
def splitDeEn(f):  <br />
     line = f.readline(); <br /> 
     de, en = line.split(',') # split De and EN entries <br />
     START: <br />
     Read the whole line <br />
     Split the English text from the German text and load to DE and EN <br />
     load tts <br />
     create audio file called line_number_de.mp3 and line_number_en.mp3 <br />
     read the German text, tts it and write it to line_number_de.mp3 <br />
     read the English text, tts it and write it to line_number_en.mp3 <br />
     save and close the files <br />
     Goto START <br />

Links:

[1] www.ocr.org.uk/Images/68532-vocabulary-list-by-topic.pdf

[2] https://developers.google.com/translate/
