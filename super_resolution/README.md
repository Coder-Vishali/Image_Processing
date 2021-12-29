# Super-resolution

This script applies super resolution effection on the image. Image super-resolution (SR) is the process of recovering high-resolution (HR) images from low-resolution (LR) images.

# Where it can be used?

When the term super-resolution is used in techniques of inferring object details from statistical treatment of the image within standard resolution limits.

# How super resolution work?
Super resolution is the process of upscaling and or improving the details within an image. Often a low resolution image is taken as an input and the same image is upscaled to a higher resolution, which is the output. The details in the high resolution output are filled in where the details are essentially unknown.

# Instruction to setup:

1. Install python 3.7 for windows 10, 64, or 32 based on your PC.
2. Configure the system environment variable by adding the following path. "C:\Users<your_Username>\AppData\Local\Programs\Python\Python37". Please change the user name accordingly.
3. Open cmd as an admin. Run "python" you should be able to python version. If yes, exit using ctrl+D or type exit(). If you are seeing an error saying "Python isn't available" or a similar error. Check for any online resource on how to configure environment variables for python.
4. Create a virtual environment for Python by providing "python -m venv virutal_environment_name"
5. cd virutal_environment_name and type Scripts\activate
6. Install the cv2 package by using "pip install opencv-python"
7. Place the .pb file into the models folder and make sure you provide the image path in line 9
8. Run "python super-resolution.py"
