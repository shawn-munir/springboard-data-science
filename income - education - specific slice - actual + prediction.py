import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, linregress
import statsmodels.formula.api as smf

os.chdir('C:\\Users\deens\OneDrive\Documents\Career\DataScienceMachineLearning\Tools\git\springboard\springboard-data-science')

gss = pd.read_hdf('gss.hdf5')

gss['age2'] = gss['age'] ** 2

gss['educ2']=gss['educ'] ** 2

results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

results_overall = smf.ols('realinc ~ educ + educ2', data=gss).fit()


mean_income_vs_educ_30yos = gss.groupby('educ')['realinc'].mean()
plt.plot(mean_income_vs_educ_30yos, label='Mean Income')
plt.xlabel('Education (Years)')
plt.ylabel('Income')


df = pd.DataFrame()
df['educ']=np.linspace(0,20)
df['educ2'] = df['educ'] ** 2
df['age']=30
df['age2']=df['age'] ** 2
income_prediction_30yos = results.predict(df)
plt.plot(df['educ'], income_prediction_30yos, label="30 Year Olds")

plt.legend()
