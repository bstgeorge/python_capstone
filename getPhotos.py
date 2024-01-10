#!/usr/local/bin/python3

import os
from PIL import Image

readDirectory = "./original"
writeDirectory = "./updated"

photos = os.listdir(path=readDirectory)

for photo in photos:
  if not photo.startswith('.'):
    with Image.open(readDirectory + "/" + photo) as im:
      outfile = writeDirectory + "/" + photo
      outfile = outfile[:-4] + ".tiff"
      print(outfile)
      im.rotate(90).resize((128, 128)).convert("RGB").save(outfile, "TIFF")

photos = os.listdir(path=writeDirectory)

for photo in photos:
  if not photo.startswith('.'):
    with Image.open(writeDirectory + "/" + photo) as im:
      print(im.format, im.size)