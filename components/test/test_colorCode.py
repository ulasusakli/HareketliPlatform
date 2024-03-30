import cv2
import numpy as np

def select_red_lower_upper(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define a region of interest (ROI) where you expect the dark red object to be
    roi = hsv[100:300, 100:300]  # Example: A 200x200 region at the center of the image

    # Calculate mean and standard deviation for each channel in the ROI
    h_mean, s_mean, v_mean = np.mean(roi, axis=(0, 1))
    h_std, s_std, v_std = np.std(roi, axis=(0, 1))

    # Define lower and upper bounds based on mean and standard deviation
    lower_red = np.array([h_mean - h_std, max(0, s_mean - s_std), max(0, v_mean - v_std)])
    upper_red = np.array([h_mean + h_std, min(255, s_mean + s_std), min(255, v_mean + v_std)])

    print("Lower Bound:", lower_red)
    print("Upper Bound:", upper_red)

# Example usage:
image_path = "src\piphototest\poz3.png"  # Path to your image
select_red_lower_upper(image_path)
