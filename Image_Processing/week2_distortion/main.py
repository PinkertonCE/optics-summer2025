import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#loading image and getting height and width as variables
img = cv.imread("Image_Processing\week2_distortion\Media\Guitar_pic.jpg")
if img is None:
    print("Image not found")

else:
    img = cv.resize(img,(600,400))

    cv.imshow("image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

h, w = img.shape[:2]


#focal length and center values
fx = fy = 800
cx = w / 2
cy = h / 2

#camera matrix

camera_matrix = np.array([
                          [fx, 0, cx],
                          [0, fy, cy]
                          [0,  0,  1]
                          ])


# distortion coefficients, k1, k2 are radial p1, p2 are tangential
#positive k barrel, negative pincushion

dist_coefficients = np.array([0.002,0.002,0,0,0])


# This map tells OpenCV how to warp the image
new_camera_matrix, _ = cv.getOptimalNewCameraMatrix(
    camera_matrix, dist_coefficients, (w, h), 1, (w, h)
)

map1, map2 = cv.initUndistortRectifyMap(
    camera_matrix, dist_coefficients, None, new_camera_matrix, (w, h), cv.CV_32FC1
)

# Remap the image using the distortion map
distorted_img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)




# Convert from BGR (OpenCV) to RGB (matplotlib)
original_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
distorted_rgb = cv.cvtColor(distorted_img, cv.COLOR_BGR2RGB)

# Set up side-by-side display
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(original_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Distorted Image")
plt.imshow(distorted_rgb)
plt.axis("off")

plt.tight_layout()
plt.show()
