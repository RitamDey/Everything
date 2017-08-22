import cv2


# Create a VideoCapture object and read from the input file
# If the input file is taken from the camera, pass 0 instead of the file name
cap = cv2.VideoCapture(0)


# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# Define the fps to be equal to 10. Also frame size is passed.
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


# Check if camera opened successfully
if cap.isOpened() is False:
    print("Error opening video stream")


# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret is True:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        # Break the loop
    else:
        break


# When everything done, realese the resources
cap.release()


# Close all the frames
cv2.destroyAllWindows()
