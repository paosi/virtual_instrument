#!/usr/bin/env python3

import os
from playsound import playsound


def name_song():

    user_name = input("What is your name? --> ")
    user_name = user_name.lower().replace(" ", "")  # Remove all whitespace from input and make lowercase
    source = os.path.join(os.getcwd(), "zapsplat", "") # Returns absolute path for the source files

    # Assign a sound to each letter. Also allow numbers and ".," characters
    for note in user_name:

        if note == "a":
            playsound(source + '001.mp3')
        elif note == "b":
            playsound(source + '002.mp3')
        elif note == "c":
            playsound(source + '003.mp3')
        elif note == "d":
            playsound(source + '004.mp3')
        elif note == "e":
            playsound(source + '005.mp3')
        elif note == "f":
            playsound(source + '006.mp3')
        elif note == "g":
            playsound(source + '007.mp3')
        elif note == "h":
            playsound(source + '008.mp3')
        elif note == "i":
            playsound(source + '009.mp3')
        elif note == "j":
            playsound(source + '010.mp3')
        elif note == "k":
            playsound(source + '011.mp3')
        elif note == "l":
            playsound(source + '012.mp3')
        elif note == "m":
            playsound(source + '013.mp3')
        elif note == "n":
            playsound(source + '014.mp3')
        elif note == "o":
            playsound(source + '015.mp3')
        elif note == "p":
            playsound(source + '016.mp3')
        elif note == "q":
            playsound(source + '017.mp3')
        elif note == "r":
            playsound(source + '018.mp3')
        elif note == "s":
            playsound(source + '019.mp3')
        elif note == "t":
            playsound(source + '020.mp3')
        elif note == "u":
            playsound(source + '021.mp3')
        elif note == "v":
            playsound(source + '022.mp3')
        elif note == "w":
            playsound(source + '023.mp3')
        elif note == "x":
            playsound(source + '024.mp3')
        elif note == "y":
            playsound(source + '025.mp3')
        elif note == "z":
            playsound(source + '026.mp3')
        elif note == ".":
            playsound(source + '027.mp3')
        elif note == ",":
            playsound(source + '028.mp3')
        elif note == "0":
            playsound(source + '029.mp3')
        elif note == "1":
            playsound(source + '030.mp3')
        elif note == "2":
            playsound(source + '031.mp3')
        elif note == "3":
            playsound(source + '032.mp3')
        elif note == "4":
            playsound(source + '033.mp3')
        elif note == "5":
            playsound(source + '034.mp3')
        elif note == "6":
            playsound(source + '035.mp3')
        elif note == "7":
            playsound(source + '036.mp3')
        elif note == "8":
            playsound(source + '037.mp3')
        elif note == "9":
            playsound(source + '038.mp3')
        else:
            # Skips any non alpha or int input
            print("Skipping {x}. {x} is not a valid letter or number".format(x = note))
            continue


name_song()
