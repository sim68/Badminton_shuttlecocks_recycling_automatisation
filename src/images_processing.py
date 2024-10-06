# images_processing.py

import picamera
import cv2
import numpy as np

def capture_image():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        camera.capture('/home/pi-volant/Images/test1.jpg')
        camera.stop_preview()

    img = cv2.imread('/home/pi-volant/Images/test1.jpg')

    # Convert the image to HSI color space
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    saturation = img_hsv[:, :, 1]

    # Isolate a region of interest (ROI)
    x_start = 900  # X coordinate of the top-left corner of the ROI
    y_start = 550  # Y coordinate of the top-left corner of the ROI
    width = 230    # Width of the ROI
    height = 400   # Height of the ROI

    isolated_zone = saturation[y_start:y_start + height, x_start:x_start + width]

    # Threshold segmentation
    threshold = 150
    segmented_image = np.zeros_like(isolated_zone)
    segmented_image[isolated_zone < threshold] = 0
    segmented_image[isolated_zone >= threshold] = 1

    # Calculate the percentage of white pixels
    total_pixels = segmented_image.size
    white_pixels = cv2.countNonZero(segmented_image)
    white_pixels_percentage = (white_pixels / total_pixels) * 100

    # Display results
    print(f"Total number of pixels: {total_pixels}")
    print(f"Number of white pixels: {white_pixels}")
    print(f"Percentage of white pixels: {white_pixels_percentage:.2f}%")

    return white_pixels_percentage
