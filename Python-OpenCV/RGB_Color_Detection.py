import cv2
import numpy as np

# taking the input from webcam
vid = cv2.VideoCapture(0)

# running while loop just to make sure that
# our program keeps running until we stop it
while True:
    # capturing the current frame
    _, frame = vid.read()

    # setting values for base colors
    b = frame[:, :, 0]  # Blue channel
    g = frame[:, :, 1]  # Green channel
    r = frame[:, :, 2]  # Red channel

    # computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    # displaying the most prominent color including black, white, and grey
    if b_mean < 50 and g_mean < 50 and r_mean < 50:
        color_text = "Black"
        color_val = (0, 0, 0)
    elif b_mean > 200 and g_mean > 200 and r_mean > 200:
        color_text = "White"
        color_val = (255, 255, 255)
    elif abs(b_mean - g_mean) < 15 and abs(g_mean - r_mean) < 15 and abs(r_mean - b_mean) < 15:
        color_text = "Grey"
        color_val = (128, 128, 128)
    elif b_mean > g_mean and b_mean > r_mean:
        color_text = "Blue"
        color_val = (255, 0, 0)
    elif g_mean > r_mean and g_mean > b_mean:
        color_text = "Green"
        color_val = (0, 255, 0)
    else:
        color_text = "Red"
        color_val = (0, 0, 255)

    # put the color text on the frame
    cv2.putText(frame, f"Color: {color_text}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                1, color_val, 2, cv2.LINE_AA)

    # displaying the current frame
    cv2.imshow("frame", frame)

    # breaking the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releasing the video capture object and closing all windows
vid.release()
cv2.destroyAllWindows()
