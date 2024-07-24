# install pillow - done
# import pillow - done
# open image using python
# print current size
# specify new size
# save new image
from PIL import Image

def resize_image(size1, size2):
    image = Image.open("myface.jpeg")

    resized_image = image.resize((size1, size2))

    resized_image.save("myface_" + str(size1) + "x" + str(size2) + ".jpeg")

    print(f"Current size: {image.size}")

size1 = int(input("Enter Length: "))
size2 = int(input("Enter Width: "))

resize_image(size1,size2)