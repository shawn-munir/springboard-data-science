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

results_overall = smf.ols('realinc ~ age + age2', data=gss).fit()

results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()
#specific for specific levels of education!! that's why need to add in them in (and quadratically since
#non-linear) since we wanna look at the relationship with/effect on income as multiple factors! as opposed to above
#overall which is NOT looking at education specifically cuz it's looking at ALL education levels OVERALL aka NOT FILTERED
#so that's why we don't need to specify it! 

mean_income_by_age = gss.groupby('age')['realinc'].mean()



gss.sort_values('age', inplace=True)
gss.reset_index(inplace=True, drop=True)


overall_income_prediction = results_overall.predict(gss)


plt.plot(mean_income_by_age, label='Mean Income')
plt.xlabel('Age')
plt.ylabel('Income')

plt.plot(gss['age'], overall_income_prediction, label="Overall")


df = pd.DataFrame()

df['age']=np.linspace(18,85)
#NOTE/REMEM, unless you specify how many points you want, it defaults to 50! i.e. dividing your range into 50 equally
#spaced points!

df['age2']=df['age'] ** 2

df['educ']=12

df['educ2'] = df['educ'] ** 2

income_prediction_HighSchool = results.predict(df)

plt.plot(df['age'], income_prediction_HighSchool, label="High School")




df['educ']=14

df['educ2'] = df['educ'] ** 2

income_prediction_Assoc = results.predict(df)

plt.plot(df['age'], income_prediction_Assoc, label="Associate's")




df['educ']=16

df['educ2'] = df['educ'] ** 2

income_prediction_Bachel = results.predict(df)

plt.plot(df['age'], income_prediction_Bachel, label="Bachelor's")


plt.legend()