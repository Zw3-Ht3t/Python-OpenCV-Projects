import cv2
import mediapipe as mp

#To convert protobuf messages to dictionaries
from google.protobuf.json_format import MessageToDict

# Initializing the Model
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2)

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

while True:
  
    # Read video frame by frame
    success, img = cap.read()

    # Flip the image(frame)
    img = cv2.flip(img, 1)

    # Convert BGR image to RGB image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image
    results = hands.process(imgRGB)

    # If hands are present in image(frame)
    if results.multi_hand_landmarks:

        # Draw bounding box for each hand
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = img.shape
            x_list = []
            y_list = []
            for lm in hand_landmarks.landmark:
                x_list.append(int(lm.x * w))
                y_list.append(int(lm.y * h))
            # Get min and max for x and y
            x_min, x_max = min(x_list), max(x_list)
            y_min, y_max = min(y_list), max(y_list)
            # Make the box square
            box_size = max(x_max - x_min, y_max - y_min)
            center_x = (x_min + x_max) // 2
            center_y = (y_min + y_max) // 2
            x1 = max(center_x - box_size // 2, 0)
            y1 = max(center_y - box_size // 2, 0)
            x2 = min(center_x + box_size // 2, w)
            y2 = min(center_y + box_size // 2, h)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # Improved: Check if both hands are present and are different (Left & Right)
        if results.multi_handedness and len(results.multi_handedness) == 2:
            labels = [MessageToDict(handedness)['classification'][0]['label'] for handedness in results.multi_handedness]
            # Only show "Both Hands" if one is Left and one is Right
            if 'Left' in labels and 'Right' in labels:
                cv2.putText(img, 'Both Hands', (250, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 0.9,
                            (0, 255, 0), 2)

        # If any hand present
        else:
            for idx, i in enumerate(results.multi_handedness):
                # Return whether it is Right or Left Hand
                label = MessageToDict(i)['classification'][0]['label']

                # Get landmarks for this hand
                hand_landmarks = results.multi_hand_landmarks[idx]
                h, w, _ = img.shape
                x_list = [int(lm.x * w) for lm in hand_landmarks.landmark]
                y_list = [int(lm.y * h) for lm in hand_landmarks.landmark]
                center_x = sum(x_list) // len(x_list)
                center_y = sum(y_list) // len(y_list)

                if label == 'Left':
                    # Display 'Left Hand' and coordinates on left side
                    cv2.putText(img, f'{label} Hand', (20, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                (0, 255, 0), 2)
                    cv2.putText(img, f'X:{center_x} Y:{center_y}', (20, 80),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                (255, 0, 0), 2)

                if label == 'Right':
                    # Display 'Right Hand' and coordinates on right side
                    cv2.putText(img, f'{label} Hand', (460, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                (0, 255, 0), 2)
                    cv2.putText(img, f'X:{center_x} Y:{center_y}', (460, 80),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                (255, 0, 0), 2)

    # Display Video and when 'q' is entered, destroy the window
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
# Release resources
cap.release()
cv2.destroyAllWindows()
