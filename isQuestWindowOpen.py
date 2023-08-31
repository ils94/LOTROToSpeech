import cv2
import numpy as np
import pyautogui
import globalVariables


def is_image_on_screen():

    image_to_detect_1 = cv2.imread("questIcon1.PNG")
    image_to_detect_2 = cv2.imread("questIcon2.PNG")

    screenshot = pyautogui.screenshot()

    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    result_1 = cv2.matchTemplate(screenshot_cv, image_to_detect_1, cv2.TM_CCOEFF_NORMED)
    min_val_1, max_val_1, min_loc_1, max_loc_1 = cv2.minMaxLoc(result_1)

    result_2 = cv2.matchTemplate(screenshot_cv, image_to_detect_2, cv2.TM_CCOEFF_NORMED)
    min_val_2, max_val_2, min_loc_2, max_loc_2 = cv2.minMaxLoc(result_2)

    if max_val_1 > 0.7 or max_val_2 > 0.7:
        return True
    else:
        globalVariables.already_talked = False
