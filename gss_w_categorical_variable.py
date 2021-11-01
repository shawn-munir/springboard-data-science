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

results = smf.ols('realinc ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()

results_logirg = smf.logit('gunlaw ~ age + age2 + educ + educ2 + + C(sex)', data=gss).fit()

#print(results_logirg.params)


# gun_vote_vs_sex = gss.groupby('sex')['gunlaw'].mean()
# plt.plot(gun_vote_vs_sex, label='Vote In Favor')
# plt.xlabel('Sex')
# plt.ylabel('Votes In Favor')

df = pd.DataFrame()
#df['sex']=np.linspace(0,1) #>>would this work??
#NOTE: this does get confusing bec we’re harping on how variables like these are discrete/
#categorical, only whole numbers, no decimals / decimals wouldn't mean anything,
#yet, we basically have to include decimals so we can spread it out and have more to plot on
#and while it may not be meaningful in most cases, in some special ones like this,
#it actually good be, where gender can be looked at as a "spectrum" and so one might be
#able to say something like the more masculine one is, the more opposed they are to gun control"

df['age']=np.linspace(18,89)
df['age2'] = df['age'] ** 2
df['educ']=12
df['educ2']=df['educ'] ** 2

df['sex']=1
gun_vote_pred_men = results_logirg.predict(df)
plt.plot(df['age'], gun_vote_pred_men, label="men")

df['sex']=2
gun_vote_pred_women = results_logirg.predict(df)
plt.plot(df['age'], gun_vote_pred_women, label="women")


#NOTE my error before was that i made the x-axis in the last/plt.plot argument df['sex'],
#even tho we set that as constants, either/or 1 & 2 for male/female
#so what that did was just make two vertical bars at x=1 & x=2. but what does that RANGE
#represent?? remem the vertical axis represents the percentage voting yes/in favor
#so that range of percentages voting yes/in favor is the range ACROSS THE AGES!!!
#that's the only loose variable here, as we're 'controlling' for / i.e. HOLDING the other
#factors in the prediction model constant!=> education & sex. (and education squared of course too
#will be constant then too
#i should've been clued that that was the target x-axis
#for here since that's what we set up on np.linspace and the others we held constant 

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