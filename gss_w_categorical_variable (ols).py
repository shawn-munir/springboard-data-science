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

# print(results.params)

df = pd.DataFrame()

df['age']=np.linspace(18,89)
df['age2'] = df['age'] ** 2
df['educ']=12
df['educ2']=df['educ'] ** 2

df['sex']=1
gun_vote_pred_men = results.predict(df)
plt.plot(df['age'], gun_vote_pred_men, label='men')

df['sex']=2
gun_vote_pred_women = results.predict(df)
plt.plot(df['age'], gun_vote_pred_women, label='women')

plt.xlabel('Age')
plt.ylabel('% Votes In Favor')
plt.legend()


#for overall actual data, regardless of sex
#gss.groupby('age')['gunlaw'].mean().plot()

#for actual data BROKEN OUT / SEPARATED BY SEX!
#simply subsetting the whole dataset, filtering for male in one and for female for the other
gss[gss['sex']==1].groupby('age')['gunlaw'].mean().plot()
gss[gss['sex']==2].groupby('age')['gunlaw'].mean().plot()

#oh yeah and we should also note that when we plot these, these include for ALL education levels, don't filter / subset
#for just educ=12 like what the prediction line comes from / is based off of


