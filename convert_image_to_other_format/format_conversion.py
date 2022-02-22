import os
from PIL import Image

def data_prepartion(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
                if os.path.isfile(os.path.join(r'C:\Users\user\Downloads\images', name[:-4]) + ".png"):
                    print("A png file already exists for %s" % name)
                else:
                    outfile = os.path.join(r'C:\Users\user\Downloads\images', name[:-4]) + ".png"
                    print(outfile)
                    im = Image.open(os.path.join(root, name))
                    print("Generating png for %s" % name)
                    im.thumbnail(im.size)
                    im.save(outfile, "png", quality=100)

if __name__ == '__main__':
    data_prepartion(r'C:\Users\user\Downloads\images')
