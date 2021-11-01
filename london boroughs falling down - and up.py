import pandas as pd
import numpy as np
import datetime as dt

properties = pd.read_excel('london.xlsx', sheet_name='Average price', index_col= None)
properties = properties.transpose()
properties = properties.reset_index()
properties.columns = properties.iloc[0]
properties = properties[1:]
properties = properties.reset_index(drop=True)
properties.rename(columns={'Unnamed: 0':'Borough'}, inplace=True)
properties.columns = properties.columns.fillna('Post Code')
properties = properties.melt(id_vars=('Borough', 'Post Code'), var_name='Date', value_name='Avg House Price')
properties['Avg House Price'] = properties['Avg House Price'].apply(pd.to_numeric)
properties = properties.dropna()

properties_start_prices = properties[properties['Date']=='1995-01-01']
properties_start_prices = properties_start_prices.sort_values('Avg House Price', ascending=False)
properties_start_prices['Rank']=range(1, 46)

properties_end_prices = properties[properties['Date']=='2021-05-01']
properties_end_prices = properties_end_prices.sort_values('Avg House Price', ascending=False)
properties_end_prices['Rank']=range(1, 46)

properties_startend_prices_ranked = properties_start_prices.merge(properties_end_prices, on='Borough', suffixes=('_1995', '_2021'))
properties_startend_prices_ranked['Rank Change'] = properties_startend_prices_ranked['Rank_1995'] - properties_startend_prices_ranked['Rank_2021']
print(properties_startend_prices_ranked)
print(properties_startend_prices_ranked.sort_values('Rank Change', ascending=False))

properties_startend_prices_ranked['Abs Rank Change'] = abs(properties_startend_prices_ranked['Rank Change'])
print(properties_startend_prices_ranked.sort_values('Abs Rank Change', ascending=False))



#attempt version 1 to add plus sign
# for i in properties_startend_prices_ranked['Rank Change']:
#     if i > 0:
#         i = "+" + str(i)
# print(properties_startend_prices_ranked)

#attempt v2 to add plus sign ;P
# for i in properties_startend_prices_ranked['Rank_1995']:
#     for j in properties_startend_prices_ranked['Rank_2021']:
#         if i - j <= 0:
#             properties_startend_prices_ranked['Rank Change'] = i - j
#         else:
#             properties_startend_prices_ranked['Rank Change'] = "+" + str(i - j)
    
#print(properties_startend_prices_ranked) #this view shows how the original ranked class stood at the end, after 26 years
#how do i make it so that if it's positive it puts a plus sign in front?'