import numpy as np
import pandas as pd

agelson = pd.DataFrame(np.array([
    [1, 2],
    [2, 17],
    [3, 6]
    ]),
    columns=['x','y'])

print(agelson['x'].corr(agelson['y']))