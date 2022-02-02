# Gelin Eguinosa Rosique
# 27-Jan-2022

import sys
from os import listdir
from os.path import isdir, join, basename


def playlist_maker(music_filenames, playlist_name, folder_path):
    """
    Creates a playlist with the names of the files specified in the list
    'music_filenames', and save them with the given 'playlist_name' + '.m3u'.
    This playlist will be saved inside the directory represented by
    'folder_path'.

    The playlist will be sorted by the filename.
    """
    # Sort the elements inside the playlist.
    sorted_filenames = sorted(music_filenames)    
    # Create the path for the playlist's file.
    playlist_path = join(folder_path, f"{playlist_name}.m3u")
    # Create the file and the save the songs of the playlist.
    with open(playlist_path, 'w') as f:
        for filename in sorted_filenames:
            f.write(filename + '\n')

def is_music(filename:str):
    """
    Determines if the music extension of filename is currently supported by the
    program.
    """
    supported_music = { '.mp3'}
    result = filename[-4:] in supported_music
    return result

def library_explorer(library_dirpath):
    """
    Explores the given Library to search for all the folders containing music
    to create a playlist with their name and the music they contain, i.e. after
    the program has run, each folder will contain a playlist (.m3u) that will
    reproduce the music they have inside.
    """
    # Lists to save the folder and music files inside the current directory.
    folderpaths = []
    music_filenames = []
    # Go through the elements of library_dirpath.
    for entry_name in listdir(library_dirpath):
        # Save the entry to its corresponding list depending if it is a song or
        # a folder.
        entry_path = join(library_dirpath, entry_name)
        if isdir(entry_path):
            folderpaths.append(entry_path)
        elif is_music(entry_path):
            music_filenames.append(entry_name)

    # Go through all the folder found in the directory and do the same process
    # of this method recursively.
    for folderpath in folderpaths:
        library_explorer(folderpath)

    # Check if we found any music in the folder and save it to a playlist with
    # same name of the directory we are currently in.
    if music_filenames:
        folder_name = basename(library_dirpath)
        playlist_maker(music_filenames, folder_name, library_dirpath)


if __name__ == '__main__':
    # This program receives the path to Music Library Folder, and creates
    # a playlist for each folder with music it finds inside.

    # Check we are receiving the proper amount of arguments.
    if len(sys.argv) != 2:
        print("\nERROR!")
        print("The program receives one argument indicating the location of",
              "the Music Library.\n")
        exit()
    # Check the argument is a folder.
    library_path = sys.argv[1]
    if not isdir(library_path):
        print("\nERROR!")
        print("The given path is not a folder.\n")
    else:
        library_explorer(library_path)
