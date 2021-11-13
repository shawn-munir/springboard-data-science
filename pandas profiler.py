import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport


df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])

profile = ProfileReport(df, title="Pandas Profiling Report")

profile2 = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

profile.to_file("your_report.html")

#OR

# As a string
json_data = profile.to_json()

# As a file
profile.to_file("your_report.json")