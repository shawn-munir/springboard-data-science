import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, linregress
import statsmodels.formula.api as smf

os.chdir('C:\\Users\deens\OneDrive\Documents\Career\DataScienceMachineLearning\Tools\git\springboard\springboard-data-science')

gss = pd.read_hdf('gss.hdf5')

mean_income_by_educ = gss.groupby('educ')['realinc'].mean()

plt.plot(mean_income_by_educ, label='Mean Income')
plt.xlabel('Education (years)')
plt.ylabel('$ Income')
plt.legend()