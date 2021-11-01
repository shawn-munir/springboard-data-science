import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
import sklearn
from scipy import stats



#open/read original

ski_data = pd.read_csv('DataScienceGuidedCapstone/raw_data/ski_resort_data.csv')
#/Users/deens/OneDrive/Documents/Career/DataScienceMachineLearning/Tools/git/springboard/springboard-data-science/DataScienceGuidedCapstone/raw_data/ski_resort_data.csv

# ski_data = ski_data[ski_data.yearsOpen < 1000]

#ski_data = ski_data[missing_price != 2]
#oh LOL - DON'T INCLUDE THIS! this was the main thing about the cleaned version - that it didn't have ones w/ missing price
#data! so we def don't wanna do that again! make sure to keep those ones w/o price data!!

# ski_data.drop(columns='fastEight', inplace=True)

# ski_data.drop(columns='AdultWeekday', inplace=True)

# ski.dropna(subset=['AdultWeekend'], inplace=True)


#SUMMARIZE BY STATE

state_summary = ski_data.groupby('state').agg(
    Total_Resorts = pd.NamedAgg('Name','count'),
    Total_Days_Open = pd.NamedAgg('daysOpenLastYear','sum'),
    Total_Terrain_Parks = pd.NamedAgg('TerrainParks','sum'),
    Total_Skiable_Acres = pd.NamedAgg('SkiableTerrain_ac','sum'),
    Total_Night_Skiing_Acres = pd.NamedAgg('NightSkiing_ac','sum'))

state_summary.replace(0, np.nan, inplace=True)
# state_summary.Total_Skiable_Acres.replace(to_replace=0,value='', inplace=True)
# state_summary.dropna(subset=['Total_Skiable_Acres'], inplace=True)

#OPEN UP EXTERNAL STATES DATA
states_url = 'https://simple.wikipedia.org/wiki/List_of_U.S._states'
usa_states = pd.read_html(states_url)

#CONVERT THIS *LIST* TO A TABLE/DF!
usa_states = usa_states[0]



#CLEAN UP EXTERNAL STATES DATA
usa_states_sub = usa_states.iloc[:, [0,6,7]].copy()
usa_states_sub.columns = ['state', 'state_population', 'state_area_sq_miles']
usa_states_sub.state.replace(to_replace='\[.*\]', value='', regex=True, inplace=True)
usa_states_sub.sort_values('state', inplace=True)
usa_states_sub.reset_index(drop=True, inplace=True)



#UPDATE STATE SUMMARY W/ MERGE W/ EXTERNAL
state_summary = state_summary.merge(usa_states_sub, on='state')


#DEFINE 2 COLUMNS - RELATIVIZE - *DERIVED* FEATURES
resorts_per_capita = (state_summary['Total_Resorts'] / state_summary['state_population']) * 100000
resorts_per_sq_mile = (state_summary['Total_Resorts'] / state_summary['state_area_sq_miles']) * 100000


state_summary['resorts_per_100kcapita'] = resorts_per_capita
state_summary['resorts_per_100ksq_mile'] = resorts_per_sq_mile
state_summary.drop(columns=['state_population', 'state_area_sq_miles'], inplace=True)
state_summary = state_summary.set_index('state')
state_summary_index = state_summary.index




#NORMALIZE / STANDARDIZE THIS STATE SUMMARY DATA!

state_summary_scaled = state_summary - state_summary.mean()     #shift everything over by the mean

# state_summary_scaled = state_summary_normalized / state_summary_normalized.std(ddof=0)  #need to spec ddof=0 cuz we got WHOLE POP! not just sample!


print("State Summary means are: ")
print(state_summary_scaled.mean())

# print("State Summary stdvs are: ")
# print(state_summary_scaled.std(ddof=0))  #again, need this here to make sure we're getting the right stdv! and indeed this does evaluate to exactly 1.0!

#this was for when we were doing the simplistic way and dividing by RANGE rather than STDV!
#print("State Summary ranges are: ")
#print(state_summary_scaled.max() - state_summary_scaled.min()) #should be equal to 1!


#variance for each column
state_summary_scaled_var = state_summary_scaled.var(ddof=0)
#this converts that into a df and assigns it a column name
state_summary_scaled_var = pd.DataFrame(state_summary_scaled_var,columns=['var'])
#sort in order of greatest variance to least, as that what PCA does!
state_summary_scaled_var.sort_values(by='var',ascending=False, inplace=True)
#this adds the percentage of each feature's variance out of the total sum variance of all features
state_summary_scaled_var['pct'] = state_summary_scaled_var / state_summary_scaled_var.sum()
#this gives us the cumulative percentage/portion of variance w/ each 'increasing' feature till we get to full 1.0
state_summary_scaled_var['cum_pct'] = state_summary_scaled_var.pct.cumsum()
#state_summary_centered_var['cum abso'] = state_summary_centered_var.cumsum()
print("State Summary variances are: ")
print(state_summary_scaled_var)

state_summary_scaled_var.plot(y='cum_pct')

print("The correlations are: ")
print(state_summary_scaled.corr().mean().sort_values(ascending=False))



#ALSO SAVE FOR LATER!!!#
# ski_data_merged = ski_data.merge(state_summary, how='left', on='state')
# ski_data_merged['resort_skiable_area_ac_state_ratio'] = ski_data_merged.SkiableTerrain_ac / ski_data_merged.Total_Skiable_Acres
# ski_data_merged['resort_days_open_state_ratio'] = ski_data_merged.daysOpenLastYear / ski_data_merged.Total_Days_Open
# ski_data_merged['resort_terrain_park_state_ratio'] = ski_data_merged.TerrainParks / ski_data_merged.Total_Terrain_Parks
# ski_data_merged['resort_night_skiing_state_ratio'] = ski_data_merged.NightSkiing_ac / ski_data_merged.Total_Night_Skiing_Acres

# ski_data_merged.drop(columns=['Total_Skiable_Acres', 'Total_Days_Open', 
#                        'Total_Terrain_Parks', 'Total_Night_Skiing_Acres'], inplace=True)


# print("The correlations are: ")
# print(ski_data_merged.corr().mean().sort_values(ascending=False))

################3
#AND THEN - IS THERE A WAY TO SORT ALLLLL THE CORR RATIOS FROM THE WHOLE TABLE???
##############3

########################
#HMMM, yeah i'm not sure why mine doesn't line up. I have a feeling it's got something to do with how we treat the 0's!!!
########################

#STORE FOR NOW...

# state_pca = PCA().fit(state_summary_scale)

# state_pca_x = state_pca.transform(state_summary_scale)


# state_avg_price = ski_data.groupby('state')['AdultWeekend'].mean()

# pca_df = pd.DataFrame({'PC1': state_pca_x[:,0], 'PC2': state_pca_x[:,1]}, index=state_summary_index)

# pca_df_state_avg_price = pd.concat([pca_df, state_avg_price, axis=1)

# pca_df_state_avg_price['Quartile'] = pd.qcut(pca_df_state_avg_price.AdultWeekend, q=4, precision=1)







