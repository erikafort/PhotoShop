'''
Erika Fortune
12/5/2017
Purpose: to create multiple different filters of an image and print the image the user asks
Help: Writing file by Paul Dickson
'''
from readwrite2PPM import *

def getInvert(im):
    '''
    Arg: the user's image filename
    Return: the new image invert
    Purpose: to invert the image
    '''
    newIm=im
    newIm[0]=255-newIm[0]
    newIm[1]=255-newIm[1]
    newIm[2]=255-newIm[2]
    return newIm

def getHopeify(im):
    '''
    Args: the user's image filename
    Return: the new image in different colors
    Purpose: to change the dark and light colors of the picture to different color 
    help by TA Kristina
    '''
    width=len(im[0])
    height=len(im)
    im2=[]
    for y in range(height):
        row=[]
        for x in range(width):
            pixel=[0,0,0]
            if(im[y][x][1]>250):
                pixel=[250,235,215]
                '''
                off white
                '''
                row.append(pixel)
            elif(im[y][x][1]>200):
                pixel=[237,33,17]
                row.append(pixel)
            elif(im[y][x][1]>150):
                pixel=[5,35,237]
                row.append(pixel)   
            elif(im[y][x][1]>25):
                pixel=[48,237,22]
                row.append(pixel)
            else:
                pixel=[0,0,0]
                row.append(pixel)
        
        im2.append(row)
    #print("width=",len(im2[0]))
    #print("height=",len(im2))
    return im2


def checkerBoard(im3):
    '''
    Args: the user's image filename
    Return: the new image with the checkerboard and inverse of the image
    Purpose: To invert the image and make it into a checker boardh
    help by alina and TA Erika at countless TA hours 
    '''
    width=len(im3[0])
    height=len(im3)
    #im2=[]
    bool = True
    a=0
    b=0
    for x in range(width):
        a=a+1
        for y in range(height):
            b=b+1
            if bool==False:
                im3[y][x] = getInvert(im3[y][x])
            for z in range(11):
                if y<(height/10)*z:
                    im3[y][x]= getInvert(im3[y][x])
                if a > width/10:
                    bool=not(bool)
                    a=0
    return im3

def saveImage(im2):
    '''
    Args: the last image created
    Return: the saved version of the image to the user's computer
    Purpose: to save the most recent image created to the user's computer
    '''
    #im2=readPPM(im2)
    writePPM("saveImage.ppm",im2)
    
def horizontalFlip(im2):
    '''
    Args: the user's image filename
    Return: the user's image flipped horizontally
    Purpose: to flip the the user's image horizontally
    '''
    width=len(im2)
    height=len(im2[0])
    new=[]

    for x in range(width):
        row=[]
        for y in range(height):
            pixel=[]
            for c in range(3):
                '''
                help by Bria
                '''
                pixel.append(im2[x][(height-1)-y][c])
                #pixel[c]=im[y][x][c]
            row.append(pixel)
        new.append(row)
    return new

def main():
    #add quit
    
    '''
    im=readPPM(filename)
    im2=readPPM(filtename)
    im3=checkerBoard(im2)
    writePPM("filename2.ppm", im3)
    '''
    filename=input("Please enter your filename as a .PPM: ")
    im=readPPM(filename)
    im2=readPPM(filename)
    im4=readPPM(filename)
    print("Here are your options (enter the number):")
    print()
    print("1.Hopeify")
    print("2.Checker Board")
    print("3.Horizontal Flip")
    print("4.Save Image")
    print("5.Quit")
    print()
    picture=input("Which filter would you like to see your picture in?")
    while(picture!="5"or picture=="quit" or picture=="Quit"):
        print(picture)
        if(picture=="1" or picture=="hopeify" or picture=="Hopeify"):
            im3=getHopeify(im2)
            print("To see your results please open 'filename2.ppm'")
            writePPM("filename2.ppm", im3)
        #picture=input("Which filter would you like to see your picture in next?")
        elif(picture=="2" or picture=="checker board" or picture=="Checker board"):
            im3=checkerBoard(im4)
            print("To see your results please open 'filename2.ppm'")
            writePPM("filename2.ppm", im3)
            #picture=input("Which filter would you like to see your picture in next?")
        elif(picture=="3" or picture=="horizontal flip" or picture=="Horizontal flip"):
            im3=horizontalFlip(im2)
            print("To see your results please open 'filename2.ppm'")
            writePPM("filename2.ppm", im3)
            #picture=input("Which filter would you like to see your picture in next?")
        elif(picture=="4" or picture=="save image"):
            im3=saveImage(im2)
            print("Open saveImage.ppm from your files to see your saved image")
            #picture=input("Which filter would you like to see your picture in next?") 
        else:    
        #if(picture!="4" or picture!="save image" or picture!="quit" or picture!="Quit" or picture!="1" or picture!="hopeify" or picture!="Hopeify"or picture!="2" or picture!="checker board" or picture!="Checker board" or picture!="3" or picture!="horizontal flip" or picture!="Horizontal flip"):
            print("Error")
            #picture=input("Please choose a new number:")
        picture=input("Which filter would you like to see your picture in next?")
    print("Program ended")
            #im3=checkerBoard(im2)
    #print("To see your results please open 'filename2.ppm'")
    #writePPM("filename2.ppm", im3)
    
main()
