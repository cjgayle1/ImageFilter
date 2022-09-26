from configparser import Interpolation
import imageio.v2 as io
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as pp
from colors import colors

imgName = input("What is the name of your image? ")

outName = input("What would you like your image to be called? ")

print("Color Styles:")
print("Style 1: Red, Blue, Tan, Light Blue (iconic Obama picture)")
print("Style 2: Green, Purple, Blue, Teal")
print("Style 3: Maroon, Grey, Light Tan")
print("Style 4: Lots of colors for a more accurate image")

colorMatrix = int(input("Which filter style would you like to use? ")) - 1


# take in image
img = io.imread(imgName)

#flattens and reshapes list for easier calulations
flatList = img.flatten().reshape(img.shape[0]*img.shape[1], img.shape[2])

#clusters colors into 
cluster = KMeans(n_clusters = len(colors[colorMatrix]), random_state = 0).fit(flatList)

#desired colors to go into the filter
colors = colors[colorMatrix]

#change colors to match filter
new_img = [colors[i] for i in cluster.labels_]
new_image = np.reshape(new_img, img.shape)

#output and save
pp.imshow(new_image, interpolation = "nearest")
pp.savefig(outName)
pp.show()
