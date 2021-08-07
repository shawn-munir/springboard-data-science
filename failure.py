import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
fig, ax = plt.subplots()
ax.hist(tips['day'])