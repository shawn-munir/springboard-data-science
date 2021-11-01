import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cats = pd.read_csv('cats.csv')

cats.groupby('color')['location'].value_counts()
