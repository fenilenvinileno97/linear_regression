import numpy as np
import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

def plot_vector(vecs, cols):
    plt.axhline(y=0, color="gray", zorder=0)
    plt.axvline(x=0, color="gray", zorder=0)
    for i in range(len(vecs)):
        x = np.concatenate(vecs[i])
        plt.quiver(
            x[0],
            x[1],
            x[2],
            x[3],
            scale_units="xy",
            scale=1,
            angles="xy",
            color=cols[i]
        )

def run():
    pass

if __name__ == "__main__":
    run()