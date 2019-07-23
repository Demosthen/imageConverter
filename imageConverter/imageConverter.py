
from PIL import Image
import os
import time
def min50(pix):
    pix=max(pix-50,0)
    return pix
def max50(pix):
    pix=min(pix+50,255)
    return pix
dirstr="trainCubes"
dirstr2="distractImgs"
dirstrT="testCubes"
dirstrT2="distractTest"
dirstrLoc="locTest"
directory=os.fsencode(dirstr)
directory2=os.fsencode(dirstr2)
directory3=os.fsencode(dirstrT)
directory4=os.fsencode(dirstrT2)
directory5=os.fsencode(dirstrLoc)
cnt1=0
cnt2=0
a=80
v=60
labels= open("labs.txt","w+")
for file in os.listdir(directory5):
        nam=os.fsdecode(file)
        fileName=dirstrLoc+"/"+nam
        #filePath="/imgs"
        im = Image.open(fileName)
        im=im.resize((320,240))
        rgbIm=im.convert("RGB")
        length,width=rgbIm.size;
        print(str(length)+" "+str(width) )
        f=open("locs/"+str(cnt1),"w+")
        f.write("1,")
        for i in range(0,length):
            for j in range(0,width):    
                r,g,b=rgbIm.getpixel((i,j))
                f.write(str(r)+","+str(g)+","+str(b)+",")
            f.write("\n")
        f.close()
        cnt1=cnt1+1
print("locDone")
cnt1=0
for file in os.listdir(directory):
    nam=os.fsdecode(file)
    fileName=dirstr+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    print(str(length)+" "+str(width) )
    f=open("cubes/"+str(cnt1),"w+")
    f.write("1,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt1=cnt1+1
print("trt1")
for file in os.listdir(directory2):
    nam=os.fsdecode(file)
    fileName=dirstr2+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=im.resize((a,v))        
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    print(str(length)+" "+str(width))
    f=open("cubes/"+str(cnt1),"w+")
    f.write("0,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt1=cnt1+1
print("trf1")

b=True
for file in os.listdir(directory3):
    nam=os.fsdecode(file)
    fileName=dirstrT+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=im.resize((a,v))
        
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    print(str(length)+" "+ str(width))
    f=open("cubeTest/"+str(cnt2),"w+")
    f.write("1,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt2=cnt2+1
print("tt1")
for file in os.listdir(directory4):
    nam=os.fsdecode(file)
    fileName=dirstrT2+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubeTest/"+str(cnt2),"w+")
    f.write("0,")
    for i in range(0,length):
        for j in range(0,width):
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt2=cnt2+1
print("tf1")
#transpose
for file in os.listdir(directory):
    nam=os.fsdecode(file)
    fileName=dirstr+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=im.transpose(Image.ROTATE_90)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubes/"+str(cnt1),"w+")
    f.write("1,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt1=cnt1+1
print("trt1")
for file in os.listdir(directory2):
    nam=os.fsdecode(file)
    fileName=dirstr2+"/"+nam
    #filePath="/imgs"
    im=im.transpose(Image.ROTATE_90)
    im = Image.open(fileName)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubes/"+str(cnt1),"w+")
    f.write("0,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt1=cnt1+1
print("trf1")
for file in os.listdir(directory3):
    nam=os.fsdecode(file)
    fileName=dirstrT+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=im.transpose(Image.ROTATE_90)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubeTest/"+str(cnt2),"w+")
    f.write("1,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt2=cnt2+1
print("tt1")
for file in os.listdir(directory4):
    nam=os.fsdecode(file)
    fileName=dirstrT2+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=im.transpose(Image.ROTATE_90)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubeTest/"+str(cnt2),"w+")
    f.write("0,")
    for i in range(0,length):
        for j in range(0,width):
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt2=cnt2+1
print("tf1")
#-50
for file in os.listdir(directory):
    nam=os.fsdecode(file)
    fileName=dirstr+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=Image.eval(im,min50)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubes/"+str(cnt1),"w+")
    f.write("1,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt1=cnt1+1
print("trt1")
for file in os.listdir(directory2):
    nam=os.fsdecode(file)
    fileName=dirstr2+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=Image.eval(im,min50)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubes/"+str(cnt1),"w+")
    f.write("0,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt1=cnt1+1
print("trf1")
for file in os.listdir(directory3):
    nam=os.fsdecode(file)
    fileName=dirstrT+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=Image.eval(im,min50)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubeTest/"+str(cnt2),"w+")
    f.write("1,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt2=cnt2+1
print("tt1")
for file in os.listdir(directory4):
    nam=os.fsdecode(file)
    fileName=dirstrT2+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=Image.eval(im,min50)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubeTest/"+str(cnt2),"w+")
    f.write("0,")
    for i in range(0,length):
        for j in range(0,width):
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt2=cnt2+1
print("tf1")
#+50
for file in os.listdir(directory):
    nam=os.fsdecode(file)
    fileName=dirstr+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=Image.eval(im,max50)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubes/"+str(cnt1),"w+")
    f.write("1,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt1=cnt1+1
print("trt1")
for file in os.listdir(directory2):
    nam=os.fsdecode(file)
    fileName=dirstr2+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=Image.eval(im,max50)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubes/"+str(cnt1),"w+")
    f.write("0,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt1=cnt1+1
print("trf1")
for file in os.listdir(directory3):
    nam=os.fsdecode(file)
    fileName=dirstrT+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=Image.eval(im,max50)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubeTest/"+str(cnt2),"w+")
    f.write("1,")
    for i in range(0,length):
        for j in range(0,width):    
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt2=cnt2+1
print("tt1")
for file in os.listdir(directory4):
    nam=os.fsdecode(file)
    fileName=dirstrT2+"/"+nam
    #filePath="/imgs"
    im = Image.open(fileName)
    im=Image.eval(im,max50)
    im=im.resize((a,v))
    rgbIm=im.convert("RGB")
    length,width=rgbIm.size;
    f=open("cubeTest/"+str(cnt2),"w+")
    f.write("0,")
    for i in range(0,length):
        for j in range(0,width):
            r,g,b=rgbIm.getpixel((i,j))
            f.write(str(r)+","+str(g)+","+str(b)+",")
        f.write("\n")
    f.close()
    cnt2=cnt2+1
print("tf1")
labels.close()

