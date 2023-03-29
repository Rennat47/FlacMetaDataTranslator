'''
@Author Tanner Smith
@Date 12/25/2022
'''
# Flac Editor
# https://mutagen.readthedocs.io/en/latest/index.html
# pip install mutagen
from mutagen.flac import FLAC

# Translation API
# https://pypi.org/project/translate-api/
# pip install translate-api
import translators as ts

# File reading
import os


def update_song_metadata(song):
    metadata_list = ['ALBUM', 'ALBUMARTIST', 'ARTIST', 'TITLE']
    audio = FLAC(song)
    # print(audio.pprint())
    for metadata in metadata_list:
        try:
            old_text = audio[metadata][0]  # this is a list to get the text we get element zero
            new_text = ts.translate_text(old_text, from_language='ja', to_language='en')
            audio[metadata] = new_text
        except KeyError:
            pass
    audio.save()
    # print(audio.pprint())


def update_song_filename(file_name, directory):
    # print(file_name)
    file_type_index = file_name.index(".flac")
    file_name = file_name[0: file_type_index]
    # print(file_name)
    new_file_name = ts.translate_text(file_name, from_language='ja', to_language='en')
    old_path = directory + "\\" + file_name + ".flac"
    new_path = directory + "\\" + new_file_name + ".flac"
    print(old_path, new_path)
    os.rename(old_path, new_path)


directory = os.getcwd()
print(directory)
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if filename.endswith('.flac'):
        print(filename)
        update_song_metadata(file_path)
        update_song_filename(filename, directory)
