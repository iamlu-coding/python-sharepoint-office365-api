from office365_api import SharePoint
import sys

# 1 args = SharePoint Folder name
FOLDER_NAME = sys.argv[1]

def get_properties_by_folder(folder):
    files_properties = SharePoint().get_file_properties_from_folder(folder)
    print('File count:', len(files_properties))
    for file in files_properties:
        print(file)
        
if __name__ == '__main__':
    get_properties_by_folder(FOLDER_NAME)