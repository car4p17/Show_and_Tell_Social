
import numpy as np
from cv2 import cv2
import os
import errno

class ImageLoader(object):
    def __init__(self, mean_file):
        self.bgr = True
        self.scale_shape = np.array([224, 224], np.int32)
        self.crop_shape = np.array([224, 224], np.int32)
        self.mean = np.load(mean_file).mean(1).mean(1)

    def load_image(self, image_file):
        """ Load and preprocess an image. """
        preprocess_folder = "./preprocessed_images/"
        preprocess_image_file = preprocess_folder + image_file[2:]
        if not "." in image_file[2:]:
            preprocess_image_file = preprocess_image_file + ".jpg"
        if os.path.exists(preprocess_image_file):
            image = cv2.imread(preprocess_image_file)
            return image

        image = cv2.imread(image_file)
        if self.bgr:
            temp = image.swapaxes(0, 2)
            temp = temp[::-1]
            image = temp.swapaxes(0, 2)

        image = cv2.resize(image, (self.scale_shape[0], self.scale_shape[1]))
        offset = (self.scale_shape - self.crop_shape) / 2
        offset = offset.astype(np.int32)
        image = image[offset[0]:offset[0]+self.crop_shape[0],
                      offset[1]:offset[1]+self.crop_shape[1]]
        image = image - self.mean
        if not os.path.exists(os.path.dirname(preprocess_image_file)):
            try:
                os.makedirs(os.path.dirname(preprocess_image_file))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        cv2.imwrite(preprocess_image_file, image)
        return image

    def load_images(self, image_files):
        """ Load and preprocess a list of images. """
        images = []
        for image_file in image_files:
            try:
                images.append(self.load_image(image_file))
            except:
                print(image_file)
                images.append(images[0])
        images = np.array(images, np.float32)
        return images
