import numpy as np
import matplotlib.pyplot as plot

data = np.genfromtxt("Fisher.txt")
data = data[1:,]

flowertype = data[:,0]

mask_for_setosa = (flowertype == 0)
setosa = data[mask_for_setosa]
#print(setosa)
mask_for_verginica = (flowertype == 1)
verginica = data[mask_for_verginica]
#print(verginica)
mask_for_versicolor = (flowertype == 2)
versicolor = data[mask_for_versicolor]
#print(versicolor)
pw_setosa = setosa[:, 1]
print("min pw of setosa:\t", pw_setosa.min())
print("mean pw of setosa:\t", pw_setosa.mean())
print("max pw of setosa:\t", pw_setosa.max())
pl_setosa = setosa[:, 2]
print("min pl of setosa:\t", pl_setosa.min())
print("mean pl of setosa:\t", pl_setosa.mean())
print("max pl of setosa:\t", pl_setosa.max())
sw_setosa = setosa[:, 3]
print("min sw of setosa:\t", sw_setosa.min())
print("mean sw of setosa:\t", sw_setosa.mean())
print("max sw of setosa:\t", sw_setosa.max())
sl_setosa = setosa[:, 4]
print("min sl of setosa:\t", sl_setosa.min())
print("mean sl of setosa:\t", sl_setosa.mean())
print("max sl of setosa:\t", sl_setosa.max())
print()
pw_verginica = verginica[:, 1]
print("min pw of verginica:\t", pw_verginica.min())
print("mean pw of setosa:\t", pw_verginica.mean())
print("max pw of verginica:\t", pw_verginica.max())
pl_verginica = verginica[:, 2]
print("min pl of verginica:\t", pl_verginica.min())
print("mean pl of verginica:\t", pl_verginica.mean())
print("max pl of verginica:\t", pl_verginica.max())
sw_verginica = verginica[:, 3]
print("min sw of verginica:\t", sw_verginica.min())
print("mean sw of verginica:\t", sw_verginica.mean())
print("max sw of verginica:\t", sw_verginica.max())
sl_verginica = verginica[:, 4]
print("min sl of verginica:\t", sl_verginica.min())
print("mean sl of verginica:\t", sl_verginica.mean())
print("max sl of verginica:\t", sl_verginica.max())
print()
pw_versicolor = versicolor[:, 1]
print("min pw of versicolor:\t", pw_versicolor.min())
print("mean pw of versicolor:\t", pw_versicolor.mean())
print("max pw of versicolor:\t", pw_versicolor.max())
pl_versicolor = versicolor[:, 2]
print("min pl of versicolor:\t", pl_versicolor.min())
print("mean pl of versicolor:\t", pl_versicolor.mean())
print("max pl of versicolor:\t", pl_versicolor.max())
sw_versicolor = versicolor[:, 3]
print("min sw of versicolor:\t", sw_versicolor.min())
print("mean sw of versicolor:\t", sw_versicolor.mean())
print("max sw of versicolor:\t", sw_versicolor.max())
sl_versicolor = versicolor[:, 4]
print("min sl of versicolor:\t", sl_versicolor.min())
print("mean sl of versicolor:\t", sl_versicolor.mean())
print("max sl of versicolor:\t", sl_versicolor.max())

plot.title("Petal and Sepal length in different species of Iris")
plot.xlabel("Petal Lenght")
plot.ylabel("Sepal Lenght")

plot.scatter(pl_setosa, sl_setosa, facecolor="red")
plot.scatter(pl_verginica, sl_verginica, facecolor="green")
plot.scatter(pl_versicolor, sl_versicolor, facecolor="blue")

plot.show()
