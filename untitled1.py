import cv2
import numpy as np

sship_img = cv2.imread('Users\Aidan\Documents\New_folder\sship.png', cv2.IMREAD_UNCHANGED)
alltypes_img = cv2.imread('Users\Aidan\Documents\New_folder\alltypes.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('alltypes', alltypes_img)
cv2.waitkey()
cv2.destroyAllWindows()

cv2.imshow('sship', sship.png)
cv2.waitkey()
cv2.destroyAllWindows()

result = cv2.matchTemplate(alltypes_img, sship_img, cv2.TM_CCOEFF_NORMED)

