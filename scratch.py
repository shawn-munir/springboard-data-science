import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

sample_means = []

for i in range(100000):
    poiss = stats.poisson.rvs(1,size=100)
    poiss_mean = np.mean(poiss)
    sample_means.append(poiss_mean)
print(poiss)

poiss_series = pd.Series(poiss)

poiss_series.hist()

#So, of course if you just draw/sample any number of numbers, it's gonna follow
#the same distribution as the probability distribution
#but to see the central limit theorem in action, you have to take the mean
#of the sample, and do that for many samples, then plot/.hist() those sample means!