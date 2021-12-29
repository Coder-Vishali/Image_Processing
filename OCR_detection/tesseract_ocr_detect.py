import pytesseract
import os
import cv2
import base64

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\<user_name>\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# ----------------------------------------------------------------
# base64 encoding the image into html img tag
# ----------------------------------------------------------------


def base64encoding(imgpath, compress_image=False):
    """
        A function which does base64 encoding the image into html img tag

        Args:
            imgpath (file): Path of the image
            compress_image (boolean): Set to False by default

        Returns:
            numpy: Encoded image
    """
    data_uri = base64.b64encode(open(imgpath, "rb").read()).decode('utf-8')
    if compress_image:
        img_tag = '<img style="width:100%" src="data:image/jpg;base64,{0}">'.format(data_uri)
    else:
        img_tag = '<img src="data:image/jpg;base64,{0}">'.format(data_uri)
    return img_tag

# creating HTML table to display results
fileout = open(os.path.join(os.path.join(os.getcwd()), "tesseract_output.html"), "w")

data = """
        <head>
            <title>Tesseract results</title>
            <style>
                table,
                th,
                td {
                    padding: 10px;
                    border: 1px solid black;
                    border-collapse: collapse;
                }
            </style>
        </head>
        <body>\n
        """

# adding columns to table
table = data + "<table>\n"
# title row
table += "<tr>\n"
table += "<th>Original image</th>\n"
table += "<th>Detected OCR</th>\n"
table += "</tr>\n"

# Mention the path of the image folder
folder = r'./images'

for filename in os.listdir(folder):
    print(f"Image_name: {filename}")
    img_cv = cv2.imread(os.path.join(folder, filename))

    # add td entries
    od_img_tag = base64encoding(os.path.join(folder, filename))

    table += "<tr>\n"
    # add these entries to html table rows
    table += f"<td>{od_img_tag}</td>\n"

    # By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
    # we need to convert from BGR to RGB format/mode:
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    ocr_text = pytesseract.image_to_string(img_rgb)
    print("Detected OCR",ocr_text)

    table += f"<td>{ocr_text}</td>"
    table += "</tr>"

# end table
table += "</table>\n</body>\n"
fileout.writelines(table)
fileout.close()
