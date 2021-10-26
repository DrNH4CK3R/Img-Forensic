
from PIL import Image
from PIL.ExifTags import TAGS
import os
import sys
import time

lgreen = '\033[92m'
cyan = '\033[96m'
bold = '\033[01m'
red = '\033[31m'
os.system("clear")

print(bold+red+"""
        ___                       ____        _
       |_ _|_ __ ___   __ _      |  _ \  __ _| |_ __ _
        | || '_ ` _ \ / _` |_____| | | |/ _` | __/ _` |
        | || | | | | | (_| |_____| |_| | (_| | || (_| |
       |___|_| |_| |_|\__, |     |____/ \__,_|\__\__,_|
                      |___/

				 Author: DrNH4CK3R
"""+red+bold)
print(cyan+"""
------------------------------------------------------------------
"""+cyan)

print("                                                       ")

# path to image

imagename = input(lgreen+">> Enter Path to Image or Video : "+lgreen)

print("                                         ")

print(lgreen+"Extractng EXIF Data....."+lgreen)

time.sleep(2)

print("                                        ")

print(lgreen+"Converting EXIF Data"+lgreen)

time.sleep(1)

print("                        ")
# read the image data using PIL

image = Image.open(imagename)

# extract EXIF data

exifdata = image.getexif()

# iterating over all EXIF data fields

for tag_id in exifdata:
	tag = TAGS.get(tag_id, tag_id)
	data = exifdata.get(tag_id)
	if isinstance(data, bytes):
		data = data.decode()
	print(cyan+bold+f"{tag:25}: {data}"+bold+cyan)

