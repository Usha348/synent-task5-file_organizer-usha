import os
import shutil

path=input("Enter path")

files=os.listdir(path)

for file in files:
    file_path=os.path.join(path,file)

    if os.path.isfile(file):
        filename,extension=os.path.split(file)
        extension=extension[1:]

        folder_path=os.path.join(path,extension)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        shutil.move(file,os.path.join(folder_path,file))
print("files organized successfully")

