import cv2
import requests

# DeepStack server URL for face recognition
deepstack_url = "https://ai.nas64.be/v1/vision/face/recognize"

# API key for DeepStack (if applicable)
api_key = ""  # Replace with your DeepStack API key or leave it as an empty string if not needed

# Capture video from the default camera (camera index 0)
cam = cv2.VideoCapture(0)

def  capture_and_recognize:
    ret, image = cam.read()
    cv2.imshow('Capture', image)

    # Wait for a key press (delay of 1 millisecond)
    key = cv2.waitKey(1)

    # Check if the 's' key is pressed (ASCII code for 's' is 115)

    # Save the captured image
    cv2.imwrite('captured_image.jpg', image)
    print("Image captured!")

    # Send the captured image to DeepStack for face recognition
    with open('captured_image.jpg', 'rb') as image_file:
    files = {"image": image_file}
    headers = {"api-key": api_key} if api_key else {}
    response = requests.post(deepstack_url, files=files, headers=headers).json()

    # Check if faces are detected in the response
    if response.get("success", False) and response.get("predictions"):
    # Assume only one face is detected
    detected_person = response["predictions"][0]["userid"]
    return(f"Detected Person: {detected_person}")
    else:
    return("No faces detected in the image.")

    # Release the camera and close all OpenCV windows
    cam.release()
    cv2.destroyAllWindows()

