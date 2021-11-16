import pandas as pd
ride_sharing = pd.read_csv('ride_sharing.csv')

duplicates = ride_sharing.duplicated(subset = 'bike_id', keep = False)

#rides_cleaned = ride_sharing.drop_duplicates(subset = 'bike_id') #keep only the first

# =============================================================================
# statistics = {'user_birth_year': 'min', 'duration': 'mean'}
# 
# ride_unique = ride_sharing.groupby('bike_id').agg(statistics).reset_index()
# 
# =============================================================================


#basically we wanna subset on the true/falses of a boolean checker

duplicated_rides = ride_sharing[duplicates]

#assert duplicated_rides.shape[0] == 0