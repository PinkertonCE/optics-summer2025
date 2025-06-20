import optics as op
import visualization as vis
import matplotlib.pyplot as plt

print("Welcome to the thin lens simulation program")

lenses = []

lens_1 = {"f": float(input("Enter Focal length and x position of lens 1:")),"x": float(input())}
lens_2 = {"f": float(input("Enter Focal length and x position of lens 2:")), "x": float(input())}

lenses.append(lens_1)
lenses.append(lens_2)

object_x = float(input("Enter object x position: ")) #cm
S_o = float(input("Enter desired object size: ")) #cm

images = []


#All calculations for images
for lens in lenses:

    #Calculations
    image_x, d_i, d_o = op.traceLens(lens["f"], lens["x"], object_x)
    M = op.magnification(d_o, d_i)
    S_i = op.imageSize(S_o, M)

    #Drawing Lenses
    vis.drawLens(S_o, S_i, lens["x"])

    #Add Image properties
    image = {"image_x": image_x, "Size": S_i}
    images.append(image)


    #Make image properties become new object properties
    object_x = image_x
    S_o = S_i


plt.show()

print(lenses)
print(images)


