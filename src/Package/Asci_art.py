from image import DrawImage 

def Ascii_Art(src):
    try:
        image = DrawImage.from_url(src)
        image.draw_image()

    except Exception as e:
        print("Error converting image to ASCII_art: ",e)