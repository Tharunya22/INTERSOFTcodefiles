# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

superman = pd.read_csv('AAPL Historical Data.csv',usecols=[0,1,2,3,4])
POHL_avg = superman[['price','open','high','low']]


obs = np.arange(1,len(superman)+1,1)
plt.plot(obs,POHL_avg,'r',label = 'my first plot')