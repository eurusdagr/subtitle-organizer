import os
import shutil
import re
import pyperclip


directory = os.chdir(input())
for file in os.listdir(directory):
    if os.path.isdir(file) == True:
        pass
    else:
        try:
         file1 = os.path.splitext(file)[0]
         pyperclip.copy(file1)
         print('name of the movie was copied to your clipboard')
         print('Insert the name of the director of the following movie: ',file1)
         foldername = input()
         if os.path.isdir(foldername) == True:
            shutil.move(file, foldername)
            print("copied file to the",foldername,"folder")
         else:
            os.mkdir(foldername)
            shutil.move(file, foldername)
            print("created",foldername,"folder and copied the file")

        except shutil.Error:
         print("fould duplacete,deleting it...")
         os.remove(file)
         pass
        except FileNotFoundError:
         pass

