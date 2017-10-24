# #Load file
# #read line by line
# def loadFile(filepath):
#     try:
#         f = open(filepath, 'r')
#         return f
#     except:
#         print("cannot open " + filepath)
#         return
#
# def splitDeEn(f):
#     line = f.readline();
#     de, en = line.split(',') # split De and EN entries
#
#     START:
#     Read the whole line
#     Split the English text from the German text and load to de and en variables
#     load tts
#     open audio file called line_number_DE and line_number_EN
#     read the German text, tts it and write it to line_number_DE
#     read the English text, tts it and write it to line_number_EN
#     save and close the two files
#     Goto START
