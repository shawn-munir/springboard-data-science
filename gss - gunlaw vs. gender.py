import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, linregress
import statsmodels.formula.api as smf

os.chdir('C:\\Users\deens\OneDrive\Documents\Career\DataScienceMachineLearning\Tools\git\springboard\springboard-data-science')

gss = pd.read_hdf('gss.hdf5')

gss.dropna(subset=['realinc', 'age', 'educ', 'gunlaw'],inplace=True)

gss['age2'] = gss['age'] ** 2

gss['educ2']=gss['educ'] ** 2

gss.gunlaw.replace(2,0, inplace=True)

results = smf.ols('gunlaw ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()

df = pd.DataFrame()

df['sex']=np.linspace(1,2)
#OKAY SO THIS WOULDN'T WORK BECAUSE WE DECLARED IT A CATEGORICAL ABOVE SO
#IT HAS TO MATCH THOSE CHOICES, CAN'T BE ANY DECIMALS! 
df['age']=45
df['age2'] = df['age'] ** 2
df['educ']=12
df['educ2']=df['educ'] ** 2

gun_vote_pred = results.predict(df)
plt.plot(df['sex'], gun_vote_pred)


plt.xlabel('Sex')
plt.ylabel('% Votes In Favor')
plt.legend()