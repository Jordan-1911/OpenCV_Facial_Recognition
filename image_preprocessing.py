import cv2
import os
import matplotlib.pyplot as plt

def process_image(image_path, face_cascade):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray)
    for i, (x, y, w, h) in enumerate(faces):
        face_gray = gray[y:y+h, x:x+w]
        
        if face_gray.size == 0:
            continue

        resized_face = cv2.resize(face_gray, (200, 200))

        filename = "processed_{}_{}".format(os.path.splitext(os.path.basename(image_path))[0], i)
        cv2.imwrite(filename + ".jpg", resized_face)

        plt.imshow(cv2.cvtColor(resized_face, cv2.COLOR_GRAY2RGB))
        plt.title("Processed Image")
        plt.show()

def main():
    face_cascade_path = "C:/Users/jorda/Documents/personal/masters/CSC515 - Computer Vision/mod3/CT2/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    image1_path = "C:/Users/jorda/Documents/personal/masters/CSC515 - Computer Vision/mod3/CT2/mugshot1.jpg"
    image2_path = "C:/Users/jorda/Documents/personal/masters/CSC515 - Computer Vision/mod3/CT2/mugshot2.jpg"

    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    process_image(image1_path, face_cascade)
    process_image(image2_path, face_cascade)

if __name__ == "__main__":
    main()


