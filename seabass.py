import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')

#sns.factorplot(data=tips, x='total_bill', y='tip', col='sex')

#sns.factorplot(data=tips, x='size', y='tip', col='sex', kind='box')
#x is disc/cat & y is continua

#sns.factorplot(data=tips, y='day', x='size', col='sex', kind='box')
#x & y are both discrete/cat

#sns.factorplot(data=tips, x='total_bill', y='tip', col='sex', kind='scatter')

#f = sns.FacetGrid(tips, col='sex')
#f.map(plt.scatter, 'tip', 'total_bill')


#sns.lmplot(data=tips, x='tip', y='total_bill', col='day', row='size')

#g = sns.PairGrid(tips, vars=['tip', 'total_bill'])

#g.map_offdiag(plt.scatter)
#g.map_diag(plt.hist)


sns.pairplot(tips, vars=['tip', 'total_bill'], diag_kind='hist')