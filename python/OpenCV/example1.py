import cv2
import numpy


# Create a VideoCapture object and read from the input file
# If the input file is taken from the camera, pass 0 instead of the file name
cap = cv2.VideoCapture(0)


# Check if camera opened successfully
if cap.isOpened() is False:
    print("Error opening video stream")


# Default resolution of the frame are obtained. The default resolutions are system dependent
# We convert the resolutions from float to integer
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# Define the fps to be equal to 10. Also frame size is passed.
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret is True:

        # Write the frame into the output file
        out.write(frame)

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
