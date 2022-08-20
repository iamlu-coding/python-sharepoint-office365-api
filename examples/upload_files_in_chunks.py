from office365_api import SharePoint
import re
import sys, os
from pathlib import PurePath

# 1 args = Root Directory Path of files to upload
ROOT_DIR = sys.argv[1]
# 2 args = SharePoint folder name. May include subfolders to upload to
SHAREPOINT_FOLDER_NAME = sys.argv[2]
# 3 args = File chunk size
CHUNK_SIZE = sys.argv[3]
# 4 args = File name pattern. Only upload files with this pattern
FILE_NAME_PATTERN = sys.argv[4]


def upload_files(folder, sharepoint_folder, chunk_size, keyword=None):
    file_list = get_list_of_files(folder)
    for file in file_list:
        if keyword is None or keyword == 'None' or re.search(keyword, file[0]):
            file_size = os.path.getsize(file[1])
            data = {'file_size': file_size}
            SharePoint().upload_file_in_chunks(file[1], sharepoint_folder, chunk_size, progress_status, **data)
            # SharePoint().upload_file_in_chunks(file[1], sharepoint_folder, chunk_size)

def get_list_of_files(folder):
    file_list = []
    folder_item_list = os.listdir(folder)
    for item in folder_item_list:
        item_full_path = PurePath(folder, item)
        if os.path.isfile(item_full_path):
            file_list.append([item, item_full_path])
    return file_list

def progress_status(offset, file_size):
    print("Uploaded '{0}' bytes from '{1}' ... '{2}'%".format(offset, file_size, round(offset/file_size * 100, 2)))

if __name__ == '__main__':
    upload_files(ROOT_DIR, SHAREPOINT_FOLDER_NAME, int(CHUNK_SIZE), FILE_NAME_PATTERN)