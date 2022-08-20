from office365_api import SharePoint
import sys
from pathlib import PurePath

# 1 args  = SharePoint Folder name
FOLDER_NAME = sys.argv[1]
# 2 args = location or remote folder destintion 
FOLDER_DEST = sys.argv[2]

def save_file(file_name, file_obj, folder_dest):
    file_dir_path = PurePath(folder_dest, file_name)
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)
        
def get_latest_file(folder, folder_dest):
    file_name, content = SharePoint().download_latest_file(folder)
    save_file(file_name, content, folder_dest)
    
if __name__ == '__main__':
    get_latest_file(FOLDER_NAME, FOLDER_DEST)
    