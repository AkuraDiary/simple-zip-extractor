import re
from zipfile import ZipFile
import os

def findZipFile_InThisDir():
    thisDir = os.getcwd()
    listDir = os.listdir(thisDir)
    rx = '(.*zip$)'
    file = ""
    fileName = ""
    
    for files in listDir:
        file = re.search(rx, files)
        if file:
            fileName = file.group()
            return fileName
        
def extract_sameDir(file_name):
    with ZipFile(file_name, 'r') as ZipObj:
        # Extract all the contents of zip file in current directory
        ZipObj.extractall()

def extract_difDir(file_name, dir):
    with ZipFile(file_name, 'r') as ZipObj:
        # Extract all the contents of zip file in the directory
        ZipObj.extractall(dir)
        
def createDir(name):
    if os.path.isdir(name):
        pass
    else:
        os.mkdir(name)

if __name__ == "__main__":

    #finding the zip file
    zipFile = findZipFile_InThisDir()

    #creating directory from the zip file name
    dir = zipFile.replace(".zip", "")
    createDir(dir)

    #extracting the zip into created dir
    extract_difDir(zipFile, dir)

    
