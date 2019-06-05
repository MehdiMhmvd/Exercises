import cv2
import numpy as np 
import matplotlib.pyplot as plt 

cap = cv2.VideoCapture(0)
while True:
	ret,frame = cap.read()
	cv2.imshow("frame", frame)

	if cv2.waitKey(1) & oxFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()
# img = cv2.imread("/home/mehdi/Downloads/watch2.jpg", cv2.IMREAD_GRAYSCALE)
# #															0
# #IMREAD_COLOR = 1
# #IMREAD_UNCHANGED = -1

# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ##Saving img 
# cv2.imwrite("/home/mehdi/Desktop/watchGray.png",img) 

# # plt.imshow(img, cmap='gray', interpolation= "bicubic")
# # plt.plot([0,50],[80,100],"c",linewidth=5)
# # plt.show()

