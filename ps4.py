
# coding: utf-8

# In[21]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
from ggplot import *


# In[28]:

filename = 'hr_year.csv'
path = './data/'


# In[29]:

data = pd.read_csv(path + filename)


# In[30]:

data.head()


# In[38]:

ggplot(data, aes(x='yearID', y='HR')) +  geom_point(color='coral') + geom_line(color='blue') +    ggtitle('Total HR by Year') + xlab('HR')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



