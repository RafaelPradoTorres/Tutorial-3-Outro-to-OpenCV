from skimage import io
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread("imagens_mastocitos/AT-PV/GC_R5_40x_AT_F16.jpg")

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)

resized = cv.resize(img, (width,height), interpolation = cv.INTER_AREA)

r = resized[:,:,0]
g = resized[:,:,1]
b = resized[:,:,2]

_,th = cv.threshold(r,90,255,cv.THRESH_BINARY)

for i in range(th.shape[0]):
    for j in range(th.shape[1]):
        if th[i,j] == 0:
            resized[i,j,0] = 255
            resized[i,j,1] = 255
            resized[i,j,2] = 255

cv.imshow("IMAGEM", resized)
cv.waitKey(0)
#plt.imshow(img)
#plt.imshow(img,cmap='gray')