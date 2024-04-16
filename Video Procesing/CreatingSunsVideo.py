import cv2
import os

path = "Images"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        file_name = path + "\\" + file
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape

size = (width, height)
print(size)

sunrise = cv2.VideoWriter("Sunrise.avi", cv2.VideoWriter_fourcc(*"XVID"), 5, size)
sunset = cv2.VideoWriter("Sunset.avi", cv2.VideoWriter_fourcc(*"XVID"), 27, size)

for i in range(count-1, 0, -1):
    frame = cv2.imread(images[i])
    sunrise.write(frame)

for i in range(0, count-1):
    frame = cv2.imread(images[i])
    sunset.write(frame)

sunset.release()
sunrise.release()
print("Done")