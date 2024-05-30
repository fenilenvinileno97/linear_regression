import numpy as np
import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

def plot_vector(vecs, cols):
    plt.axhline(y=0, color="gray", zorder=0)
    plt.axvline(x=0, color="gray", zorder=0)
    for i in range(len(vecs)):
        x = np.concatenate([[0,0], vecs[i]])
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
        
def plot_matrix_2x2(matrix, col_vector=["blue", "red"]):
    """This function helps to plot a square matrix of 2x2 dimension."""
    plt.axhline(y=0, color="gray", zorder=0)
    plt.axvline(x=0, color="gray", zorder=0)
    
    # Unit trigonometric circle
    x = np.linspace(-1, 1, 10000)
    y = np.sqrt(1-(x**2))
    
    # Matrix transformating trigonometric circle
    v1 = matrix[0,0]*x + matrix[0,1]*y
    v2 = matrix[1,0]*x + matrix[1,1]*y
    v1_neg = matrix[0,0]*x - matrix[0,1]*y
    v2_neg = matrix[1,0]*x - matrix[1,1]*y
    
    # Plotting vectors
    u = [matrix[0,0], matrix[0,1]]
    v = [matrix[1,0], matrix[1,1]]
    
    plot_vector(vecs=[u,v], cols=[col_vector[0], col_vector[1]])
    plt.plot(v1, v2, color="green", alpha=0.7)
    plt.plot(v1_neg, v2_neg, color="green", alpha=0.7)

def run():
    pass

if __name__ == "__main__":
    run()