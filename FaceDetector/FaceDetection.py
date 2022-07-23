import cv2

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = face_data.detectMultiScale(gray_img)

#face coordinates generates a 2D array and each array in it contains the coordinates of a face detected
for i in face_coordinates:
    x = i[0]
    y = i[1]
    a = i[2]
    b = i[3]
    #Drawing a rectangle on each face detected
    cv2.rectangle(img, (x, y), ((a+x), (y+ b)), (0, 255, 0), 2)

cv2.imshow('Face Detector', img)
cv2.waitKey()