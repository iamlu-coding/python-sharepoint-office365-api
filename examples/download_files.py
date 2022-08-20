from office365_api import SharePoint
import re
import sys, os
from pathlib import PurePath

# 1 args = SharePoint folder name. May include subfolders YouTube/2022
FOLDER_NAME = sys.argv[1]
# 2 args = locate or remote folder_dest
FOLDER_DEST = sys.argv[2]
# 3 args = SharePoint file name. This is used when only one file is being downloaded
# If all files will be downloaded, then set this value as "None"
FILE_NAME = sys.argv[3]
# 4 args = SharePoint file name pattern
# If no pattern match files are required to be downloaded, then set this value as "None"
FILE_NAME_PATTERN = sys.argv[4]

def save_file(file_n, file_obj):
    file_dir_path = PurePath(FOLDER_DEST, file_n)
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)

def get_file(file_n, folder):
    file_obj = SharePoint().download_file(file_n, folder)
    save_file(file_n, file_obj)

def get_files(folder):
    files_list = SharePoint()._get_files_list(folder)
    for file in files_list:
        get_file(file.name, folder)

def get_files_by_pattern(keyword, folder):
    files_list = SharePoint()._get_files_list(folder)
    for file in files_list:
        if re.search(keyword, file.name):
            get_file(file.name, folder)

if __name__ == '__main__':
    if FILE_NAME != 'None':
        get_file(FILE_NAME, FOLDER_NAME)
    elif FILE_NAME_PATTERN != 'None':
        get_files_by_pattern(FILE_NAME_PATTERN, FOLDER_NAME)
    else:
        get_files(FOLDER_NAME)