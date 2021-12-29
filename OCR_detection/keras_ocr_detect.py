import os
import cv2
import base64

try:
    import keras_ocr
    keras_ocr_available = True
except:
    print("Warning: Make sure you install keras-ocr")
    keras_ocr_available = False

    
def extract_ocr(imgarray):
    """
        A function to extract ocr

        Args:
            imgarray (numpy): This is the numpy array representation of the image

        Returns:
            numpy: This returns the recognized image representation of the given image
    """
    # Keras-ocr pipeline
    pipeline = keras_ocr.pipeline.Pipeline()
    return pipeline.recognize(imgarray)

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
fileout = open(os.path.join(os.path.join(os.getcwd()), "keras_output.html"), "w")

data = """
        <head>
            <title>Keras results</title>
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

# Path of the image folder
folder = r'./images'  

for filename in os.listdir(folder):
    print(f"Image_name: {filename}")
    img_cv = cv2.imread(os.path.join(folder, filename))

    # add td entries
    od_img_tag = base64encoding(os.path.join(folder, filename))

    table += "<tr>\n"
    # add these entries to html table rows
    table += f"<td>{od_img_tag}</td>\n"
    
    imgPath = os.path.join(folder, filename)

    prediction_groups = extract_ocr([keras_ocr.tools.read(imgPath.__str__()),])
    od_img_ocr = "".join([ocrs[0] for ocrs in prediction_groups[0]])
    print("Detected OCR",od_img_ocr)

    table += f"<td>{od_img_ocr}</td>"
    table += "</tr>"

# end table
table += "</table>\n</body>\n"
fileout.writelines(table)
fileout.close()
