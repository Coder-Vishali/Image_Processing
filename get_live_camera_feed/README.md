# Camera_feed

This script is used to receive the camera feed.

**Requirements:**

     Windows 10 (32 / 64 bit)
     Python 3.7
     
**Instruction to setup:**

1. Install python 3.7 for windows 10, 64, or 32 based on your PC.
2. Configure the system environment variable by adding the following path. "C:\Users\<your_Username>\AppData\Local\Programs\Python\Python37". Please change the user name accordingly. 
3. Open cmd as an admin. Run "python" you should be able to python version. If yes, exit using ctrl+D or type exit().  If you are seeing an error saying "Python isn't available" or a similar error.  Check for any online resource on how to configure environment variables for python. 
4. Create a virtual environment for Python by providing "python -m venv virutal_environment_name"
5. cd virutal_environment_name and type Scripts\activate
6. Install the cv2 package by using "pip install opencv-python"
7. Run "python get_camera_feed.py" 
