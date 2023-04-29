import os
import shutil
import random
import string

# Directory containing jpg images
directory = "/images"

# Loop through all files in the directory
files = os.listdir(directory)
filesCount = len(files)
random.shuffle(files)

teamMates = 2


imagesPerPerson = filesCount / teamMates

distributionDir = "/distributionImages"
for i in range(2):
    dist = os.path.join(distributionDir, str(i))
    if not os.path.exists(dist):
        os.makedirs(dist)

droppedImages = 0
currentMate = 0
for filename in files:
    img_path = os.path.join(directory, filename)
    target_path = os.path.join(distributionDir,str(currentMate), filename)

    shutil.copyfile(img_path,  target_path)

    droppedImages = droppedImages + 1
    if droppedImages >= imagesPerPerson:
        currentMate = currentMate + 1
        droppedImages = 0

