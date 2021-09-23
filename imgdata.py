
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
 ___                       _____                        _
|_ _|_ __ ___   __ _      |  ___|__  _ __ ___ _ __  ___(_) ___
 | || '_ ` _ \ / _` |_____| |_ / _ \| '__/ _ \ '_ \/ __| |/ __|
 | || | | | | | (_| |_____|  _| (_) | | |  __/ | | \__ \ | (__
|___|_| |_| |_|\__, |     |_|  \___/|_|  \___|_| |_|___/_|\___|
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

