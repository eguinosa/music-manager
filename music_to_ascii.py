# Gelin Eguinosa Rosique
# 01-Feb-2021

import eyed3
from unidecode import unidecode
from os import rename, listdir 
from os.path import join, isfile, basename


def mp3s_listdir(directory_path):
    """
    Return a list of with the paths of the mp3 files inside the folder given by
    path. It doesn't search recursively into the folders found inside this
    directory.
    """
    # List to store the mp3 files we find.
    mp3_filenames = []
    for filename in listdir(directory_path):
        # Check if the current filename belongs to a file.
        filepath = join(directory_path, filename)
        if not isfile(filepath):         
            continue
        # Check if the current file is .mp3
        if filename.endswith('.mp3'):
            mp3_filenames.append(filepath)

    # Return the final list.
    return mp3_filenames


if __name__ == '__main__':
    # Testing 'mp3s_lisdir'
    filespaths = mp3s_listdir("library/apple_music")
    for filepath in filespaths:
        print(basename(filepath))
    

