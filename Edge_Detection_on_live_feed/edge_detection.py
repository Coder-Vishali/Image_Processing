# import the necessary packages
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

i = 0
while (True):
    i = i + 1
    # Capture the video frame by frame
    ret, img = vid.read()
    rgb = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blurred, 30, 150)
    cv2.imwrite(r"edge_" + str(i) + r".jpg", canny)
    cv2.imshow('Face Mesh', canny)
    # cv2.waitKey()

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()


