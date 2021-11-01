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

results_overall = smf.ols('realinc ~ educ + educ2', data=gss).fit()
#for ALL ages, that's why we don't specifically factor in the relationship of age on income here, because for this block,
#we want the relationship of EDUCATION on income, which will include ALL ages and all of any other variables we have!
#we only specify multiple criteria when we're looking for the interactive/interaction effects of MULTIPLE factors on each
#other, like education has an impact on income, but so does age. that's what the below is for!

results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()
#factors in relationship/effect of AGE on income, in addition to effect of education on income, and describes it also 
#quadratically since that relationship too is non-linear. we need this set up here so that we input / assign / check for
#specific values of these variables, as we specify below - diff ages. in order for us to specify an age down there,
#we have to have specified that that's a variable we wanna include in our model up here, and vice versa - for us to 
#say we wanna have that as a factor variable for our model fit line up here, then we needa specify something for it 
#down below when we call it!

mean_income_by_educ = gss.groupby('educ')['realinc'].mean()



gss.sort_values('educ', inplace=True)
gss.reset_index(inplace=True, drop=True)


overall_income_prediction = results_overall.predict(gss)


plt.plot(mean_income_by_educ, label='Mean Income')
plt.xlabel('Education (Years)')
plt.ylabel('Income')

plt.plot(gss['educ'], overall_income_prediction, label="Overall")


df = pd.DataFrame()

df['educ']=np.linspace(0,20)
#NOTE/REMEM, unless you specify how many points you want, it defaults to 50! i.e. dividing your range into 50 equally
#spaced points!
df['educ2'] = df['educ'] ** 2

#FOR 30-YEAR-OLDS
df['age']=30
df['age2']=df['age'] ** 2
#####****REMEM!!!! YOU GOTTA MENTION THIS EACH TIME!!! CUZ IT'S NOT LIKE EXCEL - WON'T AUTOMATICALLY RECALCULATE THE
# COLUMN WHEN YOU PUT IN NEW VALUES/BASED ON THE NEW VALUES, EVEN THO THE COLUMN WAS CREATED WITH A FORMULA!
#IN CODING IT'S MORE LITERAL, IT'S BASED ON *SEQUENCE*! SO THE FIRST TIME WE MADE THE 'AGE2' COLUMN, IT WAS BASED
#ON SQUARING THE 'AGE' COLUMN WE HAD JUST MADE
#BUT NOW WHEN WE *REPLACE* THAT 'AGE' COLUMN, THE 'AGE2' COLUMN WILL REMAIN WHATEVER IT WAS UNTIL/UNLESS WE
#*EXPLICITLY* TELL IT OTHERWISE/I.E. MANUALLY OVERWRITE/REASSIGN IT!!!!  
income_prediction_30yo = results.predict(df)
plt.plot(df['educ'], income_prediction_30yo, label="30 Year Olds")


#40 YEAR OLDS
df['age']=40    #redefine/reassign/overwrite the age in df
df['age2']=df['age'] ** 2
income_prediction_40yo = results.predict(df)
plt.plot(df['educ'], income_prediction_40yo, label="40 Year Olds")


#50 YEAR OLDS
df['age']=50
df['age2']=df['age'] ** 2
income_prediction_50yo = results.predict(df)
plt.plot(df['educ'], income_prediction_50yo, label="50 Year Olds")


plt.legend()