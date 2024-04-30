import cv2
import numpy as np

def crop_and_save(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)

    # Rotate the image by 90 degrees
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Get the dimensions of the image
    height, width = rotated_img.shape[:2]

    # Display the width and height of the input image
    print("Cropped image width:", width)
    print("Cropped image height:", height)

    # Crop the image by specified pixels from top, bottom, left, and right
    cropped_img = rotated_img[550:height-850, 120:width-100]

    # Save the cropped image with a different name
    cv2.imwrite(output_path, cropped_img)

def divide_and_save(image_path, output_path):
    # Read the cropped image
    img = cv2.imread(image_path)

    # Get the dimensions of the cropped image
    height, width = img.shape[:2]

    # Divide the width into 3 equal parts
    section_width = width // 3

    # Create a blank image with the same dimensions as the cropped image
    divided_img = np.zeros_like(img)

    # Draw vertical lines to divide the image into 3 sections
    cv2.line(divided_img, (section_width, 0), (section_width, height), (255, 255, 0), 2)
    cv2.line(divided_img, (section_width * 2, 0), (section_width * 2, height), (255, 255, 0), 2)

    # Combine the cropped image with the lines
    divided_img = cv2.addWeighted(img, 0.7, divided_img, 0.3, 0)

    # Save the divided image
    cv2.imwrite(output_path, divided_img)

def detect_object(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image from BGR to HSV color space
    #hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for the color in  color space
    lower_red = np.array([17, 10, 100])  # Lower Color Code 
    upper_red = np.array([50, 60, 200])  # Higher Color Code

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(img, lower_red, upper_red)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    region = None  # Eğer hiç kontur bulunamazsa region'ı None olarak ayarla

    # Check if any contours are found
    if contours:
        # Get the bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(contours[0])
        
        # Determine which region the red object belongs to
        if x + w // 2 < img.shape[1] // 3:
            region = 1
        elif x + w // 2 < 2 * img.shape[1] // 3:
            region = 2
        else:
            region = 3

        # Draw the bounding box and region text on the image
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
    
    # Save the image with detected red object
    cv2.imwrite(output_path, img)

    return region 

# Provide the path to your input image
input_image_path = "src\piphototest\capture_test.jpg"  

# Example Cropped Image Function usage:
cropped_image_path = "src\piphototest\cropped_image.jpg"  # Provide the desired output path
crop_and_save(input_image_path, cropped_image_path)

# Example Divided Image Function usage:
divide_image_path = "src\piphototest\divided_image.jpg"    # Provide the desired output path
divide_and_save(cropped_image_path, divide_image_path)

# Example Color Mask Function usage:
final_image_path = "src\piphototest\Final_image.jpg"  # Path to the final image

# Result
region = detect_object(cropped_image_path, final_image_path)
print("Red Object is in:", region)
