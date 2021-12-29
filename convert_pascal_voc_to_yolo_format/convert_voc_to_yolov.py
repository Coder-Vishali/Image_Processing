import glob
import os
import xml.etree.ElementTree as ET
from os import getcwd

classes = ['cat', 'dog']
cwd = getcwd()
annotations_path = cwd + '/annotations/'
images_path = cwd + '/images/'
output_path = cwd +'/yolo/'

if not os.path.exists(output_path):
    os.makedirs(output_path)
def getImagesInDir(images_path):
    image_list = []
    for filename in glob.glob(images_path + '/*.png'):
        image_list.append(filename)
    return image_list

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(annotations_path, output_path, image_path):
    basename = os.path.basename(image_path)
    basename_no_ext = os.path.splitext(basename)[0]

    in_file = open(annotations_path + '/' + basename_no_ext + '.xml')
    out_file = open(output_path + basename_no_ext + '.txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

image_paths = getImagesInDir(images_path)
list_file = open(annotations_path + '\images.txt', 'w')

for image_path in image_paths:
    list_file.write(image_path + '\n')
    convert_annotation(annotations_path, output_path, image_path)
list_file.close()
print("Finished converting pascal VOC to Yolov format")

for image_path in image_paths:
    list_file.write(image_path + '\n')
    convert_annotation(annotations_path, output_path, image_path)
list_file.close()
img = cv2.imread(images_path)
print("Finished converting pascal VOC to Yolov format")
