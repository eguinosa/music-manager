# Gelin Eguinosa Rosique
# 01-Feb-2021

import eyed3
from unidecode import unidecode, unidecode_expect_nonascii
from os import rename, listdir
from os.path import join, isfile, basename, dirname


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


def filenames_to_ascii(filepaths):
    """
    Receive a list of files (by their paths) that may or may not be in ASCII
    encoding to renames their filenames to their respective representation in
    ASCII.

    Return a list of the files (by their paths) with their updated filenames,
    all in ASCII.
    """
    # List to store the paths of the files with their names updated to ASCII.
    final_filepaths = []
    for filepath in filepaths:
        # Check if the filename is in ASCII.
        current_filename = basename(filepath)
        if current_filename.isascii():
            # No need to update the name to ASCII.
            final_filepaths.append(filepath)
        else:
            # We have to update the file name to ASCII.
            new_filename = unidecode_expect_nonascii(current_filename)
            new_filepath = join(dirname(filepath), new_filename)
            rename(filepath, new_filepath)
            final_filepaths.append(new_filepath)

    # Return the updates filepaths, with the filenames now in ASCII.
    return final_filepaths


def tags_to_ascii(filepaths):
    """
    Receives a list of mp3 files (by their paths) and updates all their tags, so
    that name of the Artists, Album, Genre, etc. use only ASCII characters.
    
    It also removes some unnecessary information like composer or comments. This is
    a program to automate the proccess to add music to my Garmin Watch, so I
    don't need a whole lot of details about the track.
    """
    # Iterate though all the music files and update their tags.
    for filepath in filepaths:
        audiofile = eyed3.load(filepath)
        songtag = audiofile.tag
        songtag.title = unidecode(songtag.title)
        songtag.artist = unidecode(songtag.artist)
        songtag.album = unidecode(songtag.album)
        songtag.album_artist = unidecode(songtag.album_artist)
        songtag.comments.set("Music for Gelin's Garmin Watch.")
        songtag.save()



if __name__ == '__main__':
    # # Test 'mp3s_lisdir'
    # filepaths = mp3s_listdir("library/apple_music")
    # for filepath in filepaths:
    #     print(basename(filepath))

    # # Test 'filenames_to_ascii'
    # filepaths = mp3s_listdir("library/apple_music")
    # new_filepaths = filenames_to_ascii(filepaths)
    # for i in range(0, len(filepaths)):
    #     print(f"{i}: [{basename(filepaths[i])}] -> [{basename(new_filepaths[i])}]")

    # # Test eyed3
    # audiofile = eyed3.load('song.mp3')
    # current_artist = audiofile.tag.artist
    # new_artist  = unidecode(current_artist)
    # audiofile.tag.artist = "Fiesta"
    # audiofile.tag.save()
    # print(f"{current_artist} -> {new_artist}")
    
    # Test 'tags_to_ascii'
    filepaths = mp3s_listdir("library/apple_music")
    new_filepaths = filenames_to_ascii(filepaths)
    tags_to_ascii(new_filepaths)
