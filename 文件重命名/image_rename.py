import os

img_path = '/Users/cattree/Desktop/斑海豹/'

files = os.listdir(img_path)
item = 0

for file in files:
    path = img_path + file
    rename_path = img_path + str(item) + '.jpg'
    os.rename(path, rename_path)
    item = item + 1

