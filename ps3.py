
# coding: utf-8

# In[1]:
os.chdir('/Users/chrisrappoli/Documents/Coding/dataScience/introToDS')
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')


# In[2]:

filename = 'turnstile_data_master_with_weather.csv'
path = './data/'
turnstile_weather = pd.read_csv(path + filename)


# #### 1. 
# Before we perform any analysis, it might be useful to take a
# look at the data we're hoping to analyze. More specifically, let's 
# examine the hourly entries in our NYC subway data and determine what
# distribution the data follows. This data is stored in a dataframe
# called turnstile_weather under the ['ENTRIESn_hourly'] column.
# 
# Let's plot two histograms on the same axes to show hourly
# entries when raining vs. when not raining. Here's an example on how
# to plot histograms with pandas and matplotlib:
# turnstile_weather['column_to_graph'].hist()

# In[3]:

#def entries_histrogram(turnstile_weather):
#    plt.figure()


# In[4]:

# basic plotting


# In[5]:

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))


# In[6]:

ts.plot()


# In[7]:

ts_cum = ts.cumsum()


# In[8]:

ts_cum.plot()


# In[9]:

# now with dataframes


# In[10]:

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))


# In[11]:

df_cum = df.cumsum()


# In[12]:

df_cum.plot()


# In[13]:

plt.figure()
turnstile_weather[turnstile_weather['rain']==1]['ENTRIESn_hourly'].plot()
turnstile_weather[turnstile_weather['rain']==0]['ENTRIESn_hourly'].plot()


# In[ ]:

plt.clf


# In[14]:

import scipy as sp
import scipy.stats as sps


# #### 2.
# This function will consume the turnstile_weather dataframe containing
#     our final turnstile weather data. 
#     
#     You will want to take the means and run the Mann Whitney U-test on the 
#     ENTRIESn_hourly column in the turnstile_weather dataframe.
#     
#     This function should return:
#         1) the mean of entries with rain
#         2) the mean of entries without rain
#         3) the Mann-Whitney U-statistic and p-value comparing the number of entries
#            with rain and the number of entries without rain
#     
#     You should feel free to use scipy's Mann-Whitney implementation, and you 
#     might also find it useful to use numpy's mean function.

# In[15]:

entries_no_rain = turnstile_weather[turnstile_weather['rain']==0]['ENTRIESn_hourly']


# In[16]:

entries_no_rain_mean = np.mean(entries_no_rain)


# In[17]:

entries_rain = turnstile_weather[turnstile_weather['rain']==1]['ENTRIESn_hourly']


# In[18]:

entries_rain_mean = np.mean(entries_rain)


# In[19]:

mann_whiteney_results = sps.mannwhitneyu(entries_rain, entries_no_rain)


# In[20]:

mann_whiteney_results


# #### 5.
# In this question, you need to:
# 1) implement the compute_cost() and gradient_descent() procedures
# 2) Select features (in the predictions procedure) and make predictions.
# 
# The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
#     Using the information stored in the dataframe, let's predict the ridership of
#     the NYC subway using linear regression with gradient descent.
#     
#     You can download the complete turnstile weather dataframe here:
#     https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
#     
#     Your prediction should have a R^2 value of 0.40 or better.
#     You need to experiment using various input features contained in the dataframe. 
#     We recommend that you don't use the EXITSn_hourly feature as an input to the 
#     linear model because we cannot use it as a predictor: we cannot use exits 
#     counts as a way to predict entry counts. 
#     
#     Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
#     give you a random subet (~15%) of the data contained in 
#     turnstile_data_master_with_weather.csv. You are encouraged to experiment with 
#     this computer on your own computer, locally. 
#     
#     
#     If you'd like to view a plot of your cost history, uncomment the call to 
#     plot_cost_history below. The slowdown from plotting is significant, so if you 
#     are timing out, the first thing to do is to comment out the plot command again.
#     
#     If you receive a "server has encountered an error" message, that means you are 
#     hitting the 30-second limit that's placed on running your program. Try using a 
#     smaller number for num_iterations if that's the case.
#     
#     If you are using your own algorithm/models, see if you can optimize your code so 
#     that it runs faster.

# In[21]:

turnstile_weather.describe()


# In[22]:

from pandas.tools.plotting import scatter_matrix


# In[23]:

trial_data = turnstile_weather[['ENTRIESn_hourly', 'rain', 'meanwindspdi']] ##, 'maxtempi', 'precipi']]


# In[24]:

trial_data.hist()


# In[ ]:

trial_data.groupby('ENTRIESn_hourly').hist()


# In[111]:

#scatter_matrix(trial_data, alpha=0.2, figsize=(6,6), diagnal='kde')


# In[ ]:



