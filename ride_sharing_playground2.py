#cd '/Users/deens/OneDrive/Documents/Career/DataScienceMachineLearning/Tools/git/springboard/springboard-data-science/'

import pandas as pd
ride_sharing = pd.read_csv('ride_sharing.csv')


user_types = [1,2,3]

inconsistents = set(ride_sharing['user_type']).difference(user_types)

incon_rows = ride_sharing[ride_sharing['user_type'].isin(inconsistents)]
print(incon_rows)