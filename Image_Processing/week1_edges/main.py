import cv2 as cv

img = cv.imread("Test_keyboard_image.jpg")
if img is None:
    print("Image not found")

else:
    img = cv.resize(img,(600,400))

    cv.imshow("image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

#Grayscale
    grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("grayscale", grayImage)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite("grayKeyboard.jpg", grayImage)

#creates edges with grayscale image
    edges = cv.Canny(grayImage,180,220)
    cv.imshow("edges", edges)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite("keyboardEdges.jpg", edges)

#Gaussian Blur
    blur = cv.GaussianBlur(img,(5,5),0)
    cv.imshow("blur", blur)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite("blurredKeyboard.jpg",blur)


