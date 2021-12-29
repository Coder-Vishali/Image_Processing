import cv2
from os import getcwd
import glob
import os

cwd = getcwd()
images_path = cwd + '/images/'
yolov_path = cwd +'/yolo/'
output_path = cwd +'/bndbox/'

def getImagesInDir(images_path):
    image_list = []
    for filename in glob.glob(images_path + '/*.png'):
        image_list.append(filename)
    return image_list

def getyolovInDir(yolov_path):
    yolov_list = []
    for filename in glob.glob(yolov_path + '/*.txt'):
        yolov_list.append(filename)
    return yolov_list

def draw_box(image_path,yolov_path):
    img = cv2.imread(image_path)
    dh, dw, _ = img.shape
    fl = open(yolov_path, 'r')
    data = fl.readlines()
    fl.close()

    for dt in data:

        # Split string to float
        _, x, y, w, h = map(float, dt.split(' '))

        l = int((x - w / 2) * dw)
        r = int((x + w / 2) * dw)
        t = int((y - h / 2) * dh)
        b = int((y + h / 2) * dh)

        if l < 0:
            l = 0
        if r > dw - 1:
            r = dw - 1
        if t < 0:
            t = 0
        if b > dh - 1:
            b = dh - 1

        cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)

    cv2.imwrite(os.path.join(output_path, f"Cats_Test{i}.png"), img)

image_paths = getImagesInDir(images_path)
yolov_paths = getyolovInDir(yolov_path)

if not os.path.exists(output_path):
    os.makedirs(output_path)

i = 0
for image_path in image_paths:
    print("image_path", image_path)
    print(yolov_paths[i])
    draw_box(image_path, yolov_paths[i])
    i = i + 1