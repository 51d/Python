
import os
def rename_files():
    #getting file name from a drectory
    file_list = os.listdir(r"C:\udacity\python my work\prank")
    print file_list
    #renaming files
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None, "0123456789"))

rename_files()    
