# imports
from unicodedata import name
from PIL import Image
from time import sleep
import numpy as np
import os

# dictionary containing rgb -> ascii character pairs
asciiChars = {0:" ", 1:"^", 2:"@", 3:"+", 4:"="}

# number of frames in gif initially initialized to 0
numFrames = 0

# number of desired key frames
numKeyFrames = 10

# convert frames of gif to individual images
def spliceGif():
    with Image.open("sample.gif") as im:
        # number of key frames in gif
        numFrames = im.n_frames
        # searches for frame in gif and stores it -- locally -- as a separate .png file
        for i in range(numKeyFrames):
            im.seek(numFrames // numKeyFrames * i)
            im.save('frame{}.png'.format(i))
    
# convert .png representations of frames of gif to ascii text
def convertIm():
    # file type
    fileExtension = (".png")
    # iterate through all files in current working directory to locate
    # frames of gif for conversion
    for file in os.listdir():
        if file.endswith(fileExtension):
            with Image.open(file) as im:
                data = np.asarray(im)
                asciiString = ""
                for row in data:
                    for num in row:
                        try:
                            asciiString += asciiChars[sum(num)//200]
                        except:
                            pass
                    asciiString += "\n"
            # create new text file with writing permissions
            # write ascii representation of frames to text file
            with open("{}.txt".format(os.path.splitext(file)[0]), "w") as textFile:
                textFile.write(asciiString)
            # delete .png of frame
            os.remove(file)
                    
# display ascii "gif"
def displayAscii():
    # file type
    fileExtension = (".txt")
    # ascii array
    ascFrames = []
    for file in os.listdir():
        if file.endswith(fileExtension):
            # open file and store contents in string array
            # files should be in form frame1, frame2, etc...
            # hence, no checks necessary
            with open(file, "r") as textFile:
                ascFrames.append(textFile.read())   
    # infinite loop displaying "gif"
    while(1):
        for frame in ascFrames:
           print(frame, end = " ", flush = True)
           sleep(0.25)

# main method
def main():
    spliceGif()
    convertIm()
    displayAscii()

if __name__ == "__main__":
    main()