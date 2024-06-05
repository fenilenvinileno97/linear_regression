import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from seaborn import palettes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class LinearRegressionGD:
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
        
    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.b_ = np.array([0.])
        self.losses = []
        
        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w += self.eta * 2.0 * X.T.dot(errors) / X.shape[0]
            self.b_ += self.eta * 2.0 * errors.mean()
            loss = (errors**2).mean()
            self.losses_.append(loss)
        return self
    
@pd.api.extensions.register_dataframe_accessor('LinearModel')    
class LinearModel:
    def __init__(self, pandas_obj):
        self._df = pandas_obj
    
    def linear_model(self, col_x, col_y):
        """To train and test a multivariate linear model based on a set of given x data columns."""
        # Setting x_cols, which are the set of independent variables, and y_col which is the variable to predict.
        x_cols = self.obj_[col_x]
        y_col = [col_y]
        
        X = self._df[x_cols].values
        y = self._df[y_col].values

        # Normalizing variables
        X_train, X_test, y_train, y_test = train_test_split(X,y)
        sc_x = StandardScaler().fit(X) 
        sc_y = StandardScaler().fit(y)
        
        # Training the model
        X_train = sc_x.transform(X_train)
        X_test = sc_x.transform(X_test)
        y_train = sc_y.transform(y_train)
        y_test = sc_y.transform(y_test)
        
        # Testing the model
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        return y_pred
    
    def multl_model(self, col_y):
        """To train and test a multivariate linear model based on a set of x data in columns."""
        # Setting x_cols, which are the set of independent variables, and y_col which is the variable to predict.
        x_cols = list(set(self.obj_.columns)) - set([col_y])
        y_col = [col_y]
        
        X = self._df[x_cols].values
        y = self._df[y_col].values

        # Normalizing variables
        X_train, X_test, y_train, y_test = train_test_split(X,y)
        sc_x = StandardScaler().fit(X) 
        sc_y = StandardScaler().fit(y)
        
        # Training the model
        X_train = sc_x.transform(X_train)
        X_test = sc_x.transform(X_test)
        y_train = sc_y.transform(y_train)
        y_test = sc_y.transform(y_test)
        
        # Testing the model
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        return y_pred

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
    
def plot_matrix_mxn(matrix, col_vector=palettes.husl_palette):
    vecs = [vec for vec in matrix.T]
    plot_vector(vecs, cols=col_vector)

def lin_regplot(X, y, model, style="classic"):
    plt.style.use(style)
    plt.scatter(X, y, c="steelblue", edgecolor="white", s=70)
    plt.plot(X, model.predict(X), color="red", lw=2)
    
def run():
    pass

if __name__ == "__main__":
    run()