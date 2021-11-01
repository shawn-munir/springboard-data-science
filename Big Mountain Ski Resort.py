import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
import sklearn
from scipy import stats


ski_data = pd.read_csv(r'DataScienceGuidedCapstone\raw_data\ski_resort_data.csv')

#Do you even need the 'r'? cuz when i did:
#state_summary = pd.read_csv('DataScienceGuidedCapstone\data\state_summary.csv')
#it worked fine! 

missing = pd.concat([ski_data.isnull().sum(), ski_data.isnull().mean()*100], axis=1)

missing.columns = ['count', '%']

missing = missing.sort_values('count', ascending=False)

#print(missing)

#insert a new column that concats resort name with state to avoid duplicates

# where does the State NOT EQUAL the region??

mismatches = ski_data[ski_data['state']!=ski_data['Region']][['Name','state','Region']]

#mismatches['State-Region'].value_counts()

#OR

#mismatches['State-Region'].drop_duplicates()


montana = ski_data[ski_data['state']=='Montana']
montana = montana.sort_values('Name')
montana = montana.reset_index(drop=True)
montana.index+=1
montana

#sns.set_palette('Blues_r', 12)
#blues = sns.set_palette('Blues_r', 12)
#blues = sns.palplot(sns.color_palette('Blues_r', 12))
#blues = sns.color_palette('Blues_r', 12)
#colors=[sns.set_palette(['orange']) if x=='Big Mountain Resort' else sns.color_palette('Blues_r', 12) for x in montana.Name]
#ornch=['orange' for x in montana.Name if x=='Big Mountain Resort']
#sns.set_palette(blues)
#colors=[['orange'] for x in montana.Name if x=='Big Mountain Resort']

fig, ax = plt.subplots(nrows=4, ncols=2, figsize=(10,15))

blues = sns.color_palette('Blues_r', 12)    


montana.sort_values('vertical_drop', inplace=True, ascending=False)
#montana['color'] = blues
#montana.loc[montana.Name == 'Big Mountain Resort', 'color'] = 'orange'
colors_dict = dict(zip(montana.Name, blues))
colors_dict['Big Mountain Resort'] = 'orange'
vert_drop = sns.barplot(data=montana, x='Name', y='vertical_drop', palette=colors_dict, ax=ax[0,0]) #or palette=montana.color when added column method
vert_drop.set_xticklabels(vert_drop.get_xticklabels(),rotation=45, horizontalalignment='right')


montana.sort_values('summit_elev', inplace=True, ascending=False)
colors_dict = dict(zip(montana.Name, blues))
colors_dict['Big Mountain Resort'] = 'orange'
summit = sns.barplot(data=montana, x='Name', y='summit_elev', palette=colors_dict, ax=ax[0,1])
summit.set_xticklabels(summit.get_xticklabels(),rotation=45, horizontalalignment='right')



montana.sort_values('AdultWeekday', inplace=True, ascending=False)
colors_dict = dict(zip(montana.Name, blues))
colors_dict['Big Mountain Resort'] = 'orange'
price = sns.barplot(data=montana, x='Name', y='AdultWeekday', palette=colors_dict, ax=ax[1,0])
price.set_xticklabels(price.get_xticklabels(),rotation=45, horizontalalignment='right')

          
    
montana.sort_values('LongestRun_mi', inplace=True, ascending=False)
colors_dict = dict(zip(montana.Name, blues))
colors_dict['Big Mountain Resort'] = 'orange'
longest_run = sns.barplot(data=montana, x='Name', y='LongestRun_mi', palette=colors_dict, ax=ax[1,1])
longest_run.set_xticklabels(longest_run.get_xticklabels(),rotation=45, horizontalalignment='right')



montana.sort_values('Runs', inplace=True, ascending=False)
colors_dict = dict(zip(montana.Name, blues))
colors_dict['Big Mountain Resort'] = 'orange'
runs = sns.barplot(data=montana, x='Name', y='Runs', palette=colors_dict, ax=ax[2,0])
runs.set_xticklabels(runs.get_xticklabels(),rotation=45, horizontalalignment='right')



montana.sort_values('SkiableTerrain_ac', inplace=True, ascending=False)
colors_dict = dict(zip(montana.Name, blues))
colors_dict['Big Mountain Resort'] = 'orange'
skiable_area = sns.barplot(data=montana, x='Name', y='SkiableTerrain_ac', palette=colors_dict, ax=ax[2,1])
skiable_area.set_xticklabels(skiable_area.get_xticklabels(),rotation=45, horizontalalignment='right')



montana.sort_values('projectedDaysOpen', inplace=True, ascending=False)
colors_dict = dict(zip(montana.Name, blues))
colors_dict['Big Mountain Resort'] = 'orange'
daysopen = sns.barplot(data=montana, x='Name', y='projectedDaysOpen', palette=colors_dict, ax=ax[3,0])
daysopen.set_xticklabels(daysopen.get_xticklabels(),rotation=45, horizontalalignment='right')



montana.sort_values('averageSnowfall', inplace=True, ascending=False)
colors_dict = dict(zip(montana.Name, blues))
colors_dict['Big Mountain Resort'] = 'orange'
snowfall = sns.barplot(data=montana, x='Name', y='averageSnowfall', palette=colors_dict, ax=ax[3,1])
snowfall.set_xticklabels(snowfall.get_xticklabels(),rotation=45, horizontalalignment='right')




plt.subplots_adjust(wspace=.4)
plt.subplots_adjust(hspace=2)




















