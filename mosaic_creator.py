#!/usr/bin/python
#gen_collage.py - A collage generator by mattmezza
__author__ = 'mattmezza'

import sys,os,glob,math
from PIL import Image

w,h=int(sys.argv[1]),int(sys.argv[2])
r=str(sys.argv[3])
pic = (w,h)
files = glob.glob('*.jpg')
tot=len(files)
rows=math.sqrt(tot)
cols=float(tot)/rows
if r=="square":
    rows=int(rows)
    cols=int(cols)
elif r=="landscape":
    rows=int(rows/16*9)
    cols=int(cols/9*16)
else:
    rows=int(rows/9*16)
    cols=int(cols/16*9)
tw=w*cols
th=h*rows

img= Image.new('RGB',(tw,th),(0,0,0))

top=0
bottom=h
left=0
right=w
f=0
for r in range(rows):
    for c in range(cols):
        i = r*cols+cols
        small_img = Image.open(files[f]).resize((w,h), Image.ANTIALIAS)
        bbox = (left, top, right, bottom)
        img.paste(small_img,bbox)
        left+=w
        right+=w
        f+=1
    left=0
    right=w
    top+=h
    bottom+=h
os.system("mkdir -p output")
img.save("output/final.jpg", "JPEG")
