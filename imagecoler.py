import cv2
import matplotlib.pyplot as plt
image=cv2.iamread('example.jpg')
rgb=cv2.cvtcoler(image,cv2.color_BGR2RGB)
plt.imshow(rgb)
plt.title("RGBimage")
plt.show()
gray_image=cv2.cvtcoler(image,cv2.color_BGR2GRAY)
plt.imshow(gray_image,cmap='gray')
plt.title("grayscaleimage")
plt.show()
