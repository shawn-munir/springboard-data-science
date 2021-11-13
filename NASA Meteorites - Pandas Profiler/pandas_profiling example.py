%load_ext autoreload
%autoreload 2


from pathlib import Path

import requests
import numpy as np
import pandas as pd

import pandas_profiling
from pandas_profiling.utils.cache import cache_file



file_name = cache_file(
    "meteorites.csv",
    "https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD",
)

#convert this to a df. this data already exists as a table / in tabular form. just try out the csv link ^above for yourself
df = pd.read_csv(file_name)
    
# Note: Pandas does not support dates before 1880, so we ignore these for this analysis  #hain, why???

#oh wow so there's actually quite a number before that
df['year'] = pd.to_datetime(df['year'], errors='coerce')
#so this is taking the year column, and instead making it be the year column, but w/ the errors, aka years before 1880,
#'coerced', aka made NaNs, and that will be converted to date-time format


# Example: Constant variable
df['source'] = "NASA"

#ohhh ok lol, i was wondering where is the 'source' column??? but we're *MAKING* IT!! and w/ just one value, that'll
#be the value for every row, i.e. a constant


# Example: Boolean variable
df['boolean'] = np.random.choice([True, False], df.shape[0])

# Example: Mixed with base types
#hain? what's this doing?
#it's creating a column called mixed, and its values will be a random mix/selection of/between 1 & A
#df.shape[0] tells it what? to only return a single value for each cell?
df['mixed'] = np.random.choice([1, "A"], df.shape[0])


# Example: Highly correlated variables
#not sure what this is doing? taking an existing column and making a new one out of it by adding to it a randomly
#chosen number from a normal distribution w/ standard deviation of 5 (i.e. 1 stdv is 5)
#so we're literally adding a randomly chosen number from this normal distrubtion to the existing reclat's...
#but we're keeping the original col
df['reclat_city'] = df['reclat'] + np.random.normal(scale=5,size=(len(df)))

# Example: Duplicate observations
duplicates_to_add = pd.DataFrame(df.iloc[0:10])
duplicates_to_add[u'name'] = duplicates_to_add[u'name'] + " copy"

df = df.append(duplicates_to_add, ignore_index=True)

#this is gonna give us a report but we're not gonna save it
report = df.profile_report(sort=None, html={'style':{'full_width': True}}, progress_bar=False)
#Note - they had a typo - for sort had 'None' w/ quotes - invalid
report


#basically same thing, running a report, w/ a couple formatting/stylistic changes, but this time will export / save as
profile_report = df.profile_report(html={'style': {'full_width': True}})
profile_report.to_file("example.html")
#had to remove 'temp/' from/in their path


#report in a diff format/template
profile_report = df.profile_report(explorative=True, html={'style': {'full_width': True}})
profile_report


#puts it in tables&tabs form
profile_report.to_widgets()

