import os

main_directory = os.path.dirname(os.path.realpath(__file__))
files_and_folders = os.listdir(main_directory)

for _file in files_and_folders:
    _path = os.path.join(main_directory, _file)
    if os.path.isfile(_path):
        print(_file)
