import optics as op
import visualization as vis


print("Welcome to the thin lens simulation program")

f = float(input("Enter desired focal length: ")) #cm
d_o = float(input("Enter desired object distance: ")) #cm
S_o = float(input("Enter desired object size: ")) #cm

d_i = op.imageDistance(f, d_o)
M = op.magnification(d_o, d_i)
S_i = op.imageSize(S_o, M)

print(f"The image is {d_i} cm away from the lens")
print(f"The image size is {S_i} cm")

vis.drawOpticalAxis(d_o,d_i)
vis.drawLens(S_o, S_i)
vis.drawObjects(d_o, d_i, S_o, S_i)
vis.drawRays(d_o, d_i, S_o, S_i)
