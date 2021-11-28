#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:47:02 2021

@author: deens
"""

import pandas as pd

series = pd.Series(['Dr. Muhammad', 'Mrs. Misbah', 'Ms. Farrah', 'Mr. Omar', 'Miss Cago'])

replacements = {'Dr.' : '', 'Mrs.' : '', 'Ms.' : '', 'Mr.' : '', 'Miss' : ''}

series_trimmed = series.copy()

series_trimmed = series_trimmed.replace(replacements)

print(series_trimmed)


##############



replacements = {'Dr.' : '', 'Mrs.' : '', 'Ms.' : '', 'Mr.' : '', 'Miss' : ''}

airlines['full_name'] = airlines.full_name.replace(replacements)

print(airlines.full_name)