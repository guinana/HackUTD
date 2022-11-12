# Some code taken from Stack Overflow:
# https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv

# Color processing method taken from here:
# https://techtutorialsx.com/2019/04/13/python-opencv-converting-image-to-black-and-white/
import cv2

camera = cv2.VideoCapture(0) # change index 

img_num = 0

while True:
    ret, image = camera.read() # not quite sure what 'ret' is...
    ##convert to greyscale (required for black and white)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ##convert to black and white
    #(thresh, blackAndWhiteImage) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", image)
    key = cv2.waitKey(1) # 1 ms delay for key press detection

    if key%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        camera.release()
        cv2.destroyAllWindows()

    elif key % 256 == 27:
        #space pressed
        img_name = f"opencv_frame_{img_num}.png"
        cv2.imwrite(img_name, image)
        print("{} written!".format(img_name))
        img_num += 1