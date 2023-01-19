from office365_api import SharePoint
import sys, os
from pathlib import PurePath

# 1 args = SharePoint folder name. May include subfolders YouTube/2022
FOLDER_NAME = sys.argv[1]
# 2 args = locate or remote folder location
FOLDER_DEST = sys.argv[2]
# 3 args = Determine if all folders/files (subfolders) need to be downloaded
CRAWL_FOLDERS = sys.argv[3]

# save the file to locate or remote location
def save_file(file_n, file_obj, subfolder):
    dir_path = PurePath(FOLDER_DEST, subfolder)
    file_dir_path = PurePath(dir_path, file_n)
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)

# create directory if it doesn't exist
def create_dir(path):
    dir_path = PurePath(FOLDER_DEST, path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        
def get_file(file_n, folder):
    file_obj = SharePoint().download_file(file_n, folder)
    save_file(file_n, file_obj, folder)
    
def get_files(folder):
    files_list = SharePoint()._get_files_list(folder)
    for file in files_list:
        get_file(file.name, folder)
        
# get back a list of subfolders from specific folder
def get_folders(folder):
    l = []
    folder_obj = SharePoint().get_folder_list(folder)
    for subfolder_obj in folder_obj:
        subfolder = '/'.join([folder, subfolder_obj.name])
        l.append(subfolder)
    return l

if __name__ == '__main__':
    if CRAWL_FOLDERS == 'Yes':
        folder_list = get_folders(FOLDER_NAME)
        for folder in folder_list:
            for subfolder in get_folders(folder):
                folder_list.append(subfolder)
                
        folder_list[:0] = [FOLDER_NAME]
        print(folder_list)
        for folder in folder_list:
            # will create folder if it doesn't exist
            create_dir(folder)
            # get the files for specific folder location in SharePoint
            get_files(folder)
    else:
        get_files(FOLDER_NAME)