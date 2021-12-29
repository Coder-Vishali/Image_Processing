import cv2
from cv2 import dnn_superres
import time

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read image
image = cv2.imread('path_of_the_image.jpg')

# Read the desired model
path = "./models/EDSR_x4.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 4)

# Upscale the image
# use the super resolution model to upscale the image, timing how
# long it takes
start = time.time()
upscaled = sr.upsample(image)
end = time.time()
print("[INFO] Super resolution took {:.6f} seconds".format(
	end - start))

# show the spatial dimensions of the super resolution image
print("[INFO] Width: {}, Height: {}".format(upscaled.shape[1],
	upscaled.shape[0]))

# resize the image using standard bicubic interpolation
start = time.time()
bicubic = cv2.resize(image, (upscaled.shape[1], upscaled.shape[0]),
	interpolation=cv2.INTER_CUBIC)
end = time.time()

print("[INFO] Bicubic interpolation took {:.6f} seconds".format(
	end - start))

# show the original input image, bicubic interpolation image, and
# super resolution deep learning output
cv2.imshow("Original", image)
cv2.imshow("Bicubic", bicubic)
cv2.imshow("Super Resolution", upscaled)
cv2.waitKey(0)

# Save the image
cv2.imwrite("./upscaled.png", upscaled)
