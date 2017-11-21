# infinite directories
# by aaron montoya-moraga
# version 1.0.0: february 2017, stupid hackathon
# version 1.0.1: november 2017, compatible with python 3

# python script that generates infinite empty folders

#import system, string, modules
from os import system
import string

#clear the console
system("clear")

#get all of the ascii characters in lowercase
letters = string.ascii_lowercase

#initialize dirname as blank
dirname = ""

#function definition of makeFolders
#arguments are the current foldername and the ascii letters
def makeFolders(dirname, letters):
    #for every letter
    for letter in letters:
        #append the current letter to the current foldername
        dirname = dirname + letter
        #build command to pass to the terminal
        command = "mkdir " + dirname
        #send the command to the terminal
        system(command)
        #print to the terminal the name of the just created folder
        message = "created the directory " + dirname
        print(message)

# infnite loop
while(True):
    # for every letter
    for letter in letters:
        # append a new letter to the foldername
        dirname = dirname + letter
        # call to the function to create new folders
        makeFolders(dirname, letters);
