import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


london = pd.read_excel('london.xlsx', sheet_name='Average price', index_col=None)

london = london.transpose()

london.index

london = london.reset_index()

#print(london)

london.columns = london.iloc[0]

#print(london)

london = london[1:]
london = london.reset_index(drop=True)


#london.columns = london[:1]

#print(london)

london.rename(columns={'Unnamed: 0':'Borough'}, inplace=True)
london.columns = london.columns.fillna('Post Code')
#print(london)

#So then we wanna MELT and make it so that we got like a really long scroll / list of just variable and value, and pick what to keep
#So we can keep like Borough name and Post Code and then everything else like the dates and then the values separate those out line by line

london = london.melt(id_vars=('Borough', 'Post Code'), var_name='Date', value_name='Avg_House_Price')


london['Avg_House_Price'] = london['Avg_House_Price'].apply(pd.to_numeric)
#london['Avg_House_Price'].astype(float,errors='ignore')
#pd.to_numeric(london['Avg_House_Price'], errors='coerce')

london.dtypes

london.groupby('Borough').count()

london.groupby('Borough').count().count()

london[london['Borough']=='Unnamed: 47']

#london[london['Post Code'].isnull()]

london = london.dropna()

#print(london)

#london[london['Borough']=='Bexley'].plot(x='Date',y='Avg_House_Price',kind='line')

boroughs = london.drop_duplicates(subset='Borough')['Borough']

[plt.plot(london[london['Borough']==borough]['Date'],london[london['Borough']==borough]['Avg_House_Price'], label=borough) for borough in boroughs]
plt.legend()


london_maxmin = london.groupby('Borough')['Avg_House_Price'].agg([min,max])
london_maxmin['percent_increase'] = ((london_maxmin['max'] - london_maxmin['min']) / london_maxmin['min']) * 100
london_maxmin.sort_values('percent_increase', ascending=False)


london_start_prices = london[london['Date']=='1995-01-01']
london_end_prices = london[london['Date']=='2021-05-01']
london_price_change_startend = london_end_prices.merge(london_start_prices, on='Borough')
london_price_change_startend['price_change'] = london_price_change_startend['Avg_House_Price_x'] - london_price_change_startend['Avg_House_Price_y']
#london_price_change_startend.sort_values('price_change', ascending=False)
london_price_change_startend['percent_increase'] = ((london_price_change_startend['Avg_House_Price_x'] - london_price_change_startend['Avg_House_Price_y']) / london_price_change_startend['Avg_House_Price_y']) * 100
london_price_change_startend.sort_values('percent_increase', ascending=False)


london_maxmin.sort_values('percent_increase', ascending=False).head(8)
london_price_change_startend.sort_values('percent_increase', ascending=False).head(8)


#london.groupby('Borough')['Avg_House_Price']['Date']=='1998'.mean() --> dunt work - tryna figure out how to have like a filtered pivot table

###################################################333
#WAY 1: THIS WHOLE SECTION WORKS!!! aH!!!
prices1998 = london[london['Date'].dt.year==1998]
prices2018 = london[london['Date'].dt.year==2018]


avgprices1998_pivot = prices1998.pivot_table('Avg_House_Price', 'Borough', 'Date', margins=True, margins_name='Avg 1998 Price').reset_index()
avgprices2018_pivot = prices2018.pivot_table('Avg_House_Price', 'Borough', 'Date', margins=True, margins_name='Avg 2018 Price').reset_index()



avgprices1998 = avgprices1998_pivot[['Borough', 'Avg 1998 Price']]
avgprices2018 = avgprices2018_pivot[['Borough', 'Avg 2018 Price']]

avgprices1998n2018 = avgprices1998.merge(avgprices2018, on='Borough')

avgprices1998n2018['Price Ratio'] = avgprices1998n2018['Avg 2018 Price'] / avgprices1998n2018['Avg 1998 Price']

#############################################################333

#avgprices1998n2018 = avgprices1998n2018.append(avgprices1998_pivot['Avg 1998 Price'], avgprices2018_pivot['Avg 2018 Price'])  --> doesn't work, can only append one column at time?



################################################################

#WAY 2 - DICTIONARIES METHOD AND FOR LOOP! ALSO WORKS NICE!!
price_ratios={}
for borough in boroughs:
    price_ratios[borough] = borough
    avg1998price = london[(london['Borough']==borough) & (london['Date'].dt.year==1998)]['Avg_House_Price'].mean()
    avg2018price = london[(london['Borough']==borough) & (london['Date'].dt.year==2018)]['Avg_House_Price'].mean()
    price_ratio_2018_1998 = avg2018price/avg1998price
    price_ratios[borough] = avg1998price, avg2018price, price_ratio_2018_1998       #creates a dictionary key with values pairs of the above 3 calculations! 
price_ratios_df = pd.DataFrame(price_ratios).transpose()
price_ratios_df.columns = 'Avg Price 1998', 'Avg Price 2018', 'Price Ratio'
print(price_ratios_df.sort_values('Price Ratio', ascending=False))

#################################################################
#NOTE - There should also be a Way 3 & 4 to do it using .groupby() and a for loop building a dataframe from the start
#################################################################


#price_ratios_set = pd.DataFrame(columns=['Borough', 'Avg Price 1998', 'Avg Price 2018', 'Price Ratio'])        #Tried doing where I initialized a dataframe but seems to be alot harder that way
#################################################################33
#DATAFRAME METHOD
price_ratios = []
for borough in boroughs:
    avg1998price = london[(london['Borough']==borough) & (london['Date'].dt.year==1998)]['Avg_House_Price'].mean()
    avg2018price = london[(london['Borough']==borough) & (london['Date'].dt.year==2018)]['Avg_House_Price'].mean()
    price_ratio_2018_1998 = avg2018price/avg1998price
    price_ratios.append([borough, avg1998price, avg2018price, price_ratio_2018_1998])
    price_ratios_df = pd.DataFrame(price_ratios, columns=['Borough', 'Avg Price 1998', 'Avg Price 2018', 'Price Ratio'])
print(price_ratios_df.sort_values('Price Ratio', ascending=False))

#######################################################################3
#Now how do we do the above as a FUNCTION???
class create_price_ratio:
    def __init__(self, dataframe):               #so we need to declare whatever variables we're gonna be passing in for storing?
        self.dataframe = dataframe
        price_ratios = []
        for borough in boroughs: 
            avg1998price = dataframe[(dataframe['Borough']==borough) & (dataframe['Date'].dt.year==1998)]['Avg_House_Price'].mean()
            avg2018price = dataframe[(dataframe['Borough']==borough) & (dataframe['Date'].dt.year==2018)]['Avg_House_Price'].mean()
            price_ratio_2018_1998 = avg2018price/avg1998price
            price_ratios.append([borough, avg1998price, avg2018price, price_ratio_2018_1998])
            self.price_ratios_df = pd.DataFrame(price_ratios, columns=['Borough', 'Avg Price 1998', 'Avg Price 2018', 'Price Ratio'])
        print(self.price_ratios_df.sort_values('Price Ratio', ascending=False))
        
create_price_ratio(london)
        
#do we need to do like:
#london_housing_prices = create_price_ratio(london)
#london_housing_prices.price_ratio_df
        


#Basically we wanna iterate thru the list of boroughs, for each one, get the avg price in 1998 and 2018 and divide
        

# import pandas as pd
# import numpy as np
# import datetime as dt

# url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"
# properties = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col= None)
# properties = properties.transpose()
# properties = properties.reset_index()
# properties.columns = properties.iloc[0]
# properties = properties[1:]
# properties = properties.reset_index(drop=True)
# properties.rename(columns={'Unnamed: 0':'Borough'}, inplace=True)
# properties.columns = properties.columns.fillna('Post Code')
# properties = properties.melt(id_vars=('Borough', 'Post Code'), var_name='Date', value_name='Avg House Price')
# properties['Avg House Price'] = properties['Avg House Price'].apply(pd.to_numeric)
# properties = properties.dropna()









