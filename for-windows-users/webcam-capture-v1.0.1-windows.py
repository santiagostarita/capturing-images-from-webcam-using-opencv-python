# Softwares and packages required:
# 1. Python, v3.6.7
# 2. Matplotlib, v3.0.2 (to view the captured images or images that have been modified. Not required for Windows machines.) ```pip3 install matplotlib```
# 3. OpenCV, v3.4.4 ```sudo apt install python3-opencv```


import cv2
from time import sleep
key = cv2. waitKey(1)
#webcam = cv2.VideoCapture(0)

webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)  # set new dimensionns to cam object (not cap)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


sleep(2)
while True:

    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
            
            break
        
        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break
    
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break