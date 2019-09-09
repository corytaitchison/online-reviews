import statsmodels.api as sm
import numpy as np


def getNBM(x, y):
    x = sm.add_constant(np.array(x).reshape(-1, 1))
    model = sm.GLM(y, x, family=sm.families.NegativeBinomial())
    return model.fit()


def getLM(x, y):
    x = sm.add_constant(np.array(x).reshape((-1, 1)))
    model = sm.OLS(y, x)
    return model.fit()
