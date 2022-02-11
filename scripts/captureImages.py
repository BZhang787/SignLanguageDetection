import cv2
import os
import time
import uuid

IMAGES_PATH = 'C:\\Users\\brand\\RealTimeObjectDetection\\Tensorflow\\workspace\\images\\collectedimages'
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    try:
        os.makedirs(IMAGES_PATH + '\\' + label)
        print('Directory for {} was created'.format(label))
    except FileExistsError as error:
        print('Directory for {} already exists'.format(label))
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for img_num in range(number_imgs):
        ret, frame = cap.read()
        image_name = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(image_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
