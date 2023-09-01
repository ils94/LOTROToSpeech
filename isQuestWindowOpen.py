import os
import cv2
import pyautogui
import numpy as np

import globalVariables


def is_image_on_screen():
    image_files = []

    # Specify the directory path correctly
    image_directory = r"Resources/Images"

    # Iterate over files in the directory
    for filename in os.listdir(image_directory):
        # Check if the file has a common image file extension (e.g., jpg, png, jpeg)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # If it's an image file, add it to the list
            image_files.append(os.path.join(image_directory, filename))

    for image_path in image_files:
        image_to_detect = cv2.imread(image_path)

        screenshot = pyautogui.screenshot()

        screenshot_np = np.array(screenshot)
        screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(screenshot_cv, image_to_detect, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.7:
            return True
        else:
            globalVariables.already_talked = False
