# Convert-Pascal-VOC-to-Yolo-Format

This script reads PascalVOC xml files, and converts them to YOLO txt files.

**Pascal_voc:**

Used by the Pascal VOC dataset
Coordinates of a bounding box are encoded with four values in pixels: [x_min, y_min, x_max, y_max]
x_min and y_min are coordinates of the top-left corner of the bounding box
x_max and y_max are coordinates of bottom-right corner of the bounding box

**Yolo:**
A bounding box is represented by four values: [x_center, y_center, width, height]
x_center and y_center are the normalized coordinates of the center of the bounding box
To make coordinates normalized, we take pixel values of x and y, which marks the center of the bounding box on the x and y-axis.Then we divide the value of x by the width of the image and value of y by the height of the image
Width and height represent the width and the height of the bounding box. They are normalized as well


**Example of conversion:**

**Pascal voc:**
Coordinates of the example bounding box in this format are 
[98, 345, 420, 462]

**Yolov:**
Coordinates of the example bounding box in this format are 
[((420 + 98) / 2) / 640, ((462 + 345) / 2) / 480, 322 / 640, 117 / 480] 
[0.4046875, 0.840625, 0.503125, 0.24375]

Example of cat and dog detection. You can download the annotations & images from here

Link: https://www.kaggle.com/andrewmvd/dog-and-cat-detection

**Instruction to setup:**

1) Install python 3.7 for windows 10, 64 or 32 but based on your PC.  
2) Configure system environmental variable, path, by adding this line. 
"C:\Users\your_Username\AppData\Local\Programs\Python\Python37".  Please change user name accordingly. 
3) Open cmd as an admin. Run "python" you should be able to python version. If yes, exit using ctrl+D or type exit(). If you are seeing an error saying "python isn't available" or similar error. Check for any online resource, on how to configure environmental varible for python.  
4) Create a virtual environment for Python by running "python -m venv virutal_environment_name"
5) cd virutal_environment_name in cmd. And, type "Scripts\activate" to activate the virtual environment.
6) Copy the downloaded folder from this repository into this directory.  
7) Run the command "pip install -r requirements.txt"
8) Make sure you place the convert_voc_to_yolov.py file into your folder structure where you have annotations and images folder.
9) Edit the line 8 and 9 in the convert_voc_to_yolov.py script accordingly. This contain the folders where your images and xmls are located. Note: this script assumes all of your images are .png's (line 16).
10) Run the script. Results will be stored at 'yolo' folder that contains all of the YOLO txt files. 
11) Run draw_bndbox.py to draw the bounding boxes to verify the generated output of yolov results. Results of bounding boxes will be stored at "bndbox" folder
