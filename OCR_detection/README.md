# OCR Detection

Optical Character Recognition (OCR): Detects text and extracts from any image. Here, we have utilized Tesseract and Keras-ocr method to detect text

# Tesseract

Tesseract is an OCR engine with support for unicode and the ability to recognize more than 100 languages out of the box. It can be trained to recognize other languages.

# Keras-OCR

Keras-OCR is image specific OCR tool. If text is inside the image and their fonts and colors are unorganized, Keras-ocr gives good results.

# Instruction to setup
1) Install python 3.7 for windows 10, 64 or 32 but based on your PC.  
2) Configure system environmental variable, path, by adding this line. "C:\Users\your_Username\AppData\Local\Programs\Python\Python37".  Please change user name accordingly. 
3) Open cmd as an admin. Run "python" you should be able to python version. If yes, exit using ctrl+D or type exit(). If you are seeing an error saying "python isn't available" or similar error.  Check for any online resource, on how to configure environmental varible for python.  
4) Create a virtual environment for Python by running "python -m venv virutal_environment_name"
5) cd virutal_environment_name in cmd. And, type "Scripts\activate" to activate the virutal environment.  
6) Copy the downloaded folder from this repository into this directory. Run the command "pip install -r requirements.txt"
7) To use Tesseract OCR detection, Run "python tesseract_ocr_detect.py"
8) To use Keras-ocr detection, Run "python keras_ocr_detect.py"
