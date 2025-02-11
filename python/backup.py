#Auther : Sandeep R
#Description : This Python script Takes two argument as Source directory and Destination directory. It will take backup of source directory to Destination 
#              Directory. If already file exists it will append with timestamp
import os
import shutil
import sys
import datetime

if len(sys.argv) != 3: # This will check whether are we have passed 3 arguments or not
    print("execute the script ./backup.py /path of source directory  /path of destination directory")
    exit(1)

source_dir=sys.argv[1]
destination_dir=sys.argv[2]

if not os.path.exists(source_dir) or not os.path.isdir(source_dir): #This will check whether directory is available or is it directory or file
    print(f"source directory('{source_dir}') is not available")
    exit(2)

if not os.path.exists(destination_dir): #This will check whether destination directory is available or not. If not available it will create the directory
    os.makedirs(destination_dir)

for filename in os.listdir(source_dir): #This will list out all files 
    source_file=os.path.join(source_dir,filename) #This will join  one or more path
    if os.path.isfile(source_file): #This will check whether is it file or directory
        destination_file=os.path.join(destination_dir,filename)
        if os.path.isfile(source_file):
            destination_file=os.path.join(destination_dir,filename)

            if os.path.exists(destination_file): #This will check whether file is available or not
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # This will create variable of timestamp
                name, ext = os.path.splitext(filename) # This method in Python is used to split the path name into a pair root and ext
                destination_file = os.path.join(destination_dir, f"{name}_{timestamp}{ext}") 
            
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {source_file} -> {destination_file}")

