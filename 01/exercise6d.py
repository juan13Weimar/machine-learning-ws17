import numpy as np
import matplotlib.pyplot as plot


def rss(examples, w):
    """Compute the residual sum of squares for a linear model.
       
       Arguments:
       examples -- (n, p + 1)-matrix of predictors and response
       w        -- p-vector of linear model weights
    """
    x = examples[:, :-1]  # First p columns: shape = (n, p)
    y = examples.T[-1]  # Last column: shape = (n,)
    y_pred = w.dot(x.T)
    rss = (y - y_pred)**2
    ### Note: w.dot(x) has shape = (n,)
    return rss.sum()


def lms(examples, eta, iterations, print_every=1000):
    np.random.seed(2)
    rows, columns = examples.shape
    p = columns - 1  # last column is the response variable
    w = np.random.uniform(low=-1.0, high=1.0, size=p)

    for iteration in range(iterations):
        rand = np.random.randint(0, rows)  # select random index
        x = examples[rand, :-1]  # Everything but the last column
        c = examples[rand, -1:]  # The last column

        y = w.dot(x)
        error = c - y  # Error in the single chosen example
        w += (eta * error * x)

        if iteration % print_every == 0:
            print("Iteration: {} RSS: {:.2f}".format(iteration,
                                                     rss(examples, w)))
    return w

data = np.genfromtxt("Fisher.txt")
data = data[1:,]

flowertype = data[:,0]

mask_for_setosa = (flowertype == 0)
setosa = data[mask_for_setosa]
mask_for_verginica = (flowertype == 1)
verginica = data[mask_for_verginica]

sl_setosa = setosa[:,0:5:4]
sl_verginica = verginica[:,0:5:4]

###TODO: put sl_setosa and sl_verginica in the same matrix and launch the lms, the rss and display the line

plot.title("Sepal Length of Setosa and Verginica")
plot.xlabel("Sepal Lenght")
plot.ylabel("Setosa = 0, Verginica = 1")

plot.scatter(sl_setosa[:,1], sl_setosa[:,0], facecolor="red")
plot.scatter(sl_verginica[:,1], sl_verginica[:,0], facecolor="green")

plot.show()
