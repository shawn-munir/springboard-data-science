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
print(results.params)



mean_income_by_age = gss.groupby('age')['realinc'].mean()
plt.plot(mean_income_by_age)
plt.xlabel('Age')
plt.ylabel('Income')














df = pd.DataFrame()

df['age']=np.linspace(18,85)

df['educ']=12

df['age2']=df['age'] ** 2

df['educ2'] = df['educ'] ** 2

income_prediction_HighSchool = results.predict(df)
#this is saying to apply the params of the results of the original gss dataset which calculate the slope between
#each variable and the prediction one - to the df we just came up with specifying an age, education level, etc
#so this is taking those result parameters of predicting income from these 4 other fields and making a single
#prediction out of it, given ALL of that! what the income should be!


plt.plot(mean_income_by_age, label="Mean Income")
#and this will once again be the mean income plot over / across the ages


plt.plot(df['age'], income_prediction, label="High School")
#and then we wanna see what that prediction is of income over/across age at / w/ a highest education level of High School
#so this will simply plot the single income prediction $ y-value over/for the given x-->age
#this is telling us what the income should be for THESE SPECIFIED AGES AND EDUCATION LEVEL, GIVEN THE PARAMS IT FOUND
#FROM THE OG DATASET!
#we could have also looked at it across ONE age, over the different education levels
#so that would be what an individual at a particular age could expect to earn across the range of education levels (below)


df['educ']=14

df['educ2'] = df['educ'] ** 2

income_prediction_Assoc = results.predict(df)

plt.plot(df['age'], income_prediction_Assoc, label="Associate's")




df['educ']=16

df['educ2'] = df['educ'] ** 2

income_prediction_Bachel = results.predict(df)

plt.plot(df['age'], income_prediction_Bachel, label="Bachelor's")






#so having both of these plotted superimposed okay so this is gonna plot the ACTUAL data as well as
#OUR MODEL PREDICTION!
#and as we see the fit line is pretty good!

#so we've been plotting actual data then trying to find the best fit line, which is the prediction line

plt.xlabel('Age')
plt.ylabel('Income')
plt.legend()



#1. Plot the ACTUAL data: income over age
#2. Then we made extra quadratic columns for our non-linear variables (with income!) of interest: age and education
#   (So that means if we plot age^2 vs. income we should see linear??)
#   Hmmm...tried it, but (shape) looked exactly the same
#3. Then we made a results wrapper containing the params like intersection and slope of predicting income/rise
#   as a result of age, age^2, educ & educ^2
#4. Then use the predict function to get the single predicted value, aka income, from these 4 variables
#5. Then we plotted these predictions on top of our actual data to see how well the predictions lined up / fared
#   against our actual data and the shape did at least match! Got the non-linear / quadratic shape down
#   (rather than our standard straight linear regression / trend / best fit line)!
# SO HOW DO WE RECONCILE THE 'SLOPE' FROM RESULTS, WHICH IS ONLY FOR STRAIGHT LINES, RIGHT? WITH THE PARABOLA OF .PREDICT() 







# #Pick one age
# df2 = pd.DataFrame()
# df2['age']=45   #choose this cuz it's like the middle of the range

# df2['age2']=df2['age'] ** 2

# df2['educ']=np.linspace(0,20)

# df2['educ2'] = df2['educ'] ** 2

# results2 = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# income_prediction2 = results2.predict(df2)

# plt.plot(df2['educ'], income_prediction2, label="Age 45")


#so 'results' is the set of regression results like slope, intercept, corr(?), etc. it's a 'results wrapper'
#it's the results for the predicted change in income for these 4 params / the effect of these 4 params on income

# mean_income_by_age2 = gss.groupby('age2')['realinc'].mean()
# plt.plot(mean_income_by_age2)
# plt.xlabel('Age^2')
# plt.ylabel('Income')


# results1 = smf.ols('realinc ~ educ', data=gss).fit()
# print(results1.params)

# results2 = smf.ols('realinc ~ educ + age', data=gss).fit()
# print(results2.params)

# results3 = smf.ols('realinc ~ age', data=gss).fit()
# print(results3.params)

#this will let us see how income changes with education, i.e. the slope
#so for every year of education, how much does income go up?
#>> $3,586.52

# income['portion'] = income / income.count()

# income['cum'] = income.portion.cumsum()

# income.cum.plot()