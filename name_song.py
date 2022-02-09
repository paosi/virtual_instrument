#!/usr/bin/env python3

import os
from playsound import playsound


def name_song(user_name):

    user_name = user_name.lower().replace(" ", "")  # Remove all whitespace from input and make lowercase
    source = os.path.join(os.getcwd(), "zapsplat", "") # Returns absolute path for the source files

    # Assign a sound to each letter. Also allow numbers and ".," characters
    for note in user_name:
        
        match note:
            case "a":
                playsound(source + '001.mp3')
            case "b":
                playsound(source + '002.mp3')
            case "c":
                playsound(source + '003.mp3')
            case "d":
                playsound(source + '004.mp3')
            case "e":
                playsound(source + '005.mp3')
            case "f":
                playsound(source + '006.mp3')
            case "g":
                playsound(source + '007.mp3')
            case "h":
                playsound(source + '008.mp3')
            case "i":
                playsound(source + '009.mp3')
            case "j":
                playsound(source + '010.mp3')
            case "k":
                playsound(source + '011.mp3')
            case "l":
                playsound(source + '012.mp3')
            case "m":
                playsound(source + '013.mp3')
            case "n":
                playsound(source + '014.mp3')
            case "o":
                playsound(source + '015.mp3')
            case "p":
                playsound(source + '016.mp3')
            case "q":
                playsound(source + '017.mp3')
            case "r":
                playsound(source + '018.mp3')
            case "s":
                playsound(source + '019.mp3')
            case "t":
                playsound(source + '020.mp3')
            case "u":
                playsound(source + '021.mp3')
            case "v":
                playsound(source + '022.mp3')
            case "w":
                playsound(source + '023.mp3')
            case "x":
                playsound(source + '024.mp3')
            case "y":
                playsound(source + '025.mp3')
            case "z":
                playsound(source + '026.mp3')
            case ".":
                playsound(source + '027.mp3')
            case ",":
                playsound(source + '028.mp3')
            case "0":
                playsound(source + '029.mp3')
            case "1":
                playsound(source + '030.mp3')
            case "2":
                playsound(source + '031.mp3')
            case "3":
                playsound(source + '032.mp3')
            case "4":
                playsound(source + '033.mp3')
            case "5":
                playsound(source + '034.mp3')
            case "6":
                playsound(source + '035.mp3')
            case "7":
                playsound(source + '036.mp3')
            case "8":
                playsound(source + '037.mp3')
            case "9":
                playsound(source + '038.mp3')
            case _ :
                # Skips any non alpha or int input
                print("Skipping {x}. {x} is not a valid letter or number".format(x = note))
                continue


if __name__ == "__main__":

    user_name = input("What is your name? --> ")
    name_song(user_name)
