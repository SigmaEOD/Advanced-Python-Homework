import os
import shutil
def stu_activities():
    #Specifies The Download Folder
    download_folder = os.path.expanduser('~\Downloads')
    #Specifies the Current Working Directory
    currentdir = os.getcwd() 
    #Walks through and finds the slides files
    for root, dirs, files in os.walk(download_folder):
        for file in files:
            if 'readme' in file.lower():
                readme = (os.path.join(root, file))
                print(readme)
                shutil.copy(readme, currentdir)
                #Copy File
stu_activities()