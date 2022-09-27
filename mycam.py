import cv2

cap = cv2.VideoCapture(0)

ret, photo = cap.read()

cv2.imwrite('/root/Desktop/vimal.png',photo)

cap.release()

#Put pd.rules at location /etc/udev/rules.d