# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

# To set resolutions, it is required to convert values from float to integer.
frame_width = int(vid.get(3))
frame_height = int(vid.get(4))

# get the size of the frame
size = (frame_width, frame_height)

# Below VideoWriter object will create a frame of above defined 
# The output is stored in 'filename.mp4' file.
result = cv2.VideoWriter('filename.mp4',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
i = 0
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # To save each frame
    cv2.imwrite('frame' + str(i) + '.jpg', frame)
    
    i += 1
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
