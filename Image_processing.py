from PIL import Image

# img  = Image.open(path)
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)
def main():
    try:
        img = Image.open("C:\Users\mittariy\Documents\My Received Files\images.jpg" )
        print img
        width,  height=img.size
        print width,height
        imformat=img.format
        print imformat
        #img.show()
        #img.rotate(-90).show()
        area=(0,0,width/2,height/2)
        #img.crop(area).show()
        img.save("C:\images.jpg")
        print img.histogram()
        print img.split()
        print img.tobitmap()
        #img.show()
        #img.save("C:\Users\mittariy\Documents\My Received Files\images_1.jpg")
        #img.show()
    except IOError:
        pass

if __name__=="__main__":
    main()

# Use the above statem
# raise an IOError if file cannot be found,
# or image cannot be opened.