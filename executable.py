#infinite directories
#done for the stupid hackathon
#by aaron montoya-moraga
#february 2017

#import system, time, string modules
from os import system
import string

#clear the console
system("clear")

#get all of the ascii characters in lowercase
letters = string.ascii_lowercase

#initialize dirname as blank
dirname = ""

#function definition of makeNewFolders
#arguments are the current foldername and the ascii letters
def makeNewDirs(dirname, letters):
    #for every letter
    for letter in letters:
        #append the current letter to the current foldername
        dirname = dirname + letter
        #build command to pass to the terminal
        command = "mkdir " + dirname
        #send the command to the terminal
        system(command)
        #print to the terminal the name of the just created directory
        print "created the directory " + dirname

#infnite looop
while(True):
    #for every letter
    for letter in letters:
        #append a new letter to the foldername
        dirname = dirname + letter
        #call to the
        makeNewDirs(dirname, letters);
