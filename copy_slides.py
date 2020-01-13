import os
import shutil
def pptx_copy():
    #Specifies The Download Folder
    download_folder = os.path.expanduser('~\Downloads')
    #Specifies the Current Working Directory
    currentdir = os.getcwd() 
    #Walks through and finds the slides files
    for root, dirs, files in os.walk(download_folder):
        for file in files:
            if file.endswith(".pptx"):
                pptx = (os.path.join(root, file))
                #Copy File
                shutil.copy(pptx, currentdir)
            if file.endswith(".ppt"):
                ppt = (os.path.join(root, file))
                #Copy File
                shutil.copy(ppt, currentdir)
pptx_copy()