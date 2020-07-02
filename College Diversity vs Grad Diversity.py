#!/usr/bin/env python
# coding: utf-8

# In[31]:


pip install datascience


# In[199]:


from datascience import *
path_data = '../../../data/'
import numpy as np
import matplotlib
matplotlib.use('Agg', warn=False)
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
import pandas as pd
plots.style.use('fivethirtyeight')


# # Overview: Campus Diversity vs Graduation Diversity 
# 
# Prospective students, concerned parents, and enrolled students are all bombarded with pamphlets from colleges that boast on their campus diveristy. But they don't seem to be as transparent about who gets to make it to graduation. In this reseach project we will discuss the the precense of minorities on UC campuses vs the amount of minorities who actually recive degrees. 
# 
# #### Research Questions: 
#     
#     What are UC campusus diveristy rates on campus compared to those actually earn a degree?
#     
#     What UC campuses have the most diversity in both on campus and in graduates?
#     
#     How diverse is the UC system as a whole? 
# 
# It is important to ask these questions especially when higher education has proven to be apart of systemic racism. With this study we will be looking at the UCs Specifically beuause they are one of the most applied to universities in the world. With so many applicants we can expect a diverse pool which then leads to diverse class rooms and ultimately a diverse graduating class. But, what this study finds is that each UC seems to have their own agenda on what students they are admitting and what students they help succeed. 
# 
# # Meathods
#     
# All data reflects fall 2019. Since a lot of the data was in PDF form I have do manually create the tables. When gatherign the data I only used the top 5 reoccuring race boxes since they vary from campus to campus. I decided to include Black, Native, Latinx/Hispanic, Asian, White since they were acessible on all campuses. 
# 
# Once all data was gathered I used those categories as thier own 100%. I created percentages for campus demographics and grad demographics for each campus and for the UC System as a whole. 
# 
# ### Data limitations: 
# Since not all campuses categorized race the same it was difficult to create my own categories. The data was also manually imported so it will not be as accurate as imported form csv files. 
# 
# ### Sources Used: 
# 
#     https://www.univstats.com 
#      
#      UC fall enrollment 2019 Data sheet

# # This link will take you do a slide presentation on data collected from the study. 
# 
# https://drive.google.com/file/d/1Nf8WTwiuxDMhj14_L0ZFUe-r22WjLDBN/view?usp=sharing

# In[202]:


Race = make_array("Black", "Native American", "Latinx/Hispanic", "Asian", "White")
Race


# In[168]:


#ALL UC Campuses Demographics

Campus_Percentage = make_array("4.1%", "0.5%", "24.8%", "33.5%", "21.4%")
Campus_Count = make_array("9,371 students", "1,065 students", "55,971 students", "75,676 students", "48,433 students" )

UC_Demographics = Table().with_columns(
    "Race", Race,
    "UC Demographics by Percentage", Campus_Percentage,
    "UC Demographics Count", Campus_Count)
UC_Demographics


# In[170]:


#ALL UC CAMPUS GRAD STATS

Campus_Percentage_Grad = make_array("2.2%", "0.1%", "21.2%", "40.7%", "26.1%")
Campus_Count_Grad = make_array("722 students", "40 students","6,817 students", "13,105 students", "8,404 students")

UC_GRAD = Table().with_columns(
    "Race", Race,
    "UC Grad Demographics by Percentage", Campus_Percentage_Grad,
    "UC Demographics Count", Campus_Count_Grad)
UC_GRAD


# In[121]:


#UC BERKELEY CAMPUS DEMOGRAPHICS
# BLACK 3% (843 students), Native Americans 1%(186),
# Hispanic 13%, Asian 40% (9,990 students)
# White 29% (7,243 students)

Campus_Percentage_Berk = make_array("3.4%", "0.04%", "15.5%", "39.8%", "23.9%")
Campus_Count_Berk = make_array("1,084 students", "138 studnets", "4861 students", "12,497 students", "7,509 students")

UC_BERKELEY_DEMOGRAPHICS = Table().with_columns(
    "Race", Race,
    "Campus Demographics by Percentage", Campus_Percentage_Berk,
    "Campus Demographic Count",Campus_Count_Berk )
UC_BERKELEY_DEMOGRAPHICS


# In[147]:


#UC BERKELEY GRADUATION STATS
#These stats are for students who actually completed their BS degree, not just attended comencement

# BLACK 76.60% (72 students), Native 75%(3 students),
# Hispanic 85.29% (429 students), Asian 95.45% (1,554 students)
# White 91.22% (966 students)

Grad_Percentage_Berk = make_array("1.9%", "0.07%", "11.3%","41.1%", "25.6%")
Grad_Count_Berk = ("72 students", "3 students", "429 students", "1554 students", "966 students")

UC_BERKELEY_GRADUATION = Table().with_columns(
    "Race", Race,
    "Grad Demographics by Percentage", Grad_Percentage_Berk,
    "Grad Demographic Count", Grad_Count_Berk
)
UC_BERKELEY_GRADUATION


# In[148]:


#UCLA CAMPUS DEMOGRAPHICS

Campus_Percentage_UCLA = make_array("3.3%", "0.2%","22.3%", "27.6%", "26.3%")
Campus_Count_UCLA = make_array("1,057 students", "70 students", "7,056 students", "8,731 students","8,310 students")
UCLA_CAMPUS_DEMOGRAPHICS = Table().with_columns(
    "Race", Race,
    "Campus Demographics by Percentage", Campus_Percentage_UCLA,
    "Campus Demographic Count", Campus_Count_UCLA)
UCLA_CAMPUS_DEMOGRAPHICS


# In[150]:


#UCLA GRADUATION STATS

Grad_Percentage_UCLA = make_array("2%", "0.05%", "17.5%","31.1%", "24.3%")
Grad_Count_UCLA = make_array("102 students", "5 students", "891 students", "1,582 students", "1,233 students")
UCLA_GRADUATION = Table().with_columns(
    "Race", Race,
    "Grad Demographics by Percentage", Grad_Percentage_UCLA,
    "Grad Demographic Count", Grad_Count_UCLA)
UCLA_GRADUATION


# In[125]:


#UCSC CAMPUS DEMOGRAPHICS 

Campus_Percentage_UCSC = make_array("4.3%", "0.8%", "25.3%", "27.6%", "31.1%")
Campus_Count_UCSC = make_array("752 students", "147 students", "4,428 students", "4,834 students", "5,438 students")
UCSC_CAMPUS_DEMOGRAPHICS = Table().with_columns(
    "Race", Race,
    "Campus Demographics by Percentage", Campus_Percentage_UCSC,
    "Campus Demographic Count", Campus_Count_UCSC)
UCSC_CAMPUS_DEMOGRAPHICS


# In[151]:


#UCSC GRADUATION STATS

Grad_Percentage_UCSC = make_array("1.6%", "0.07%","32.2%", "25.6%", "33%")
Grad_Count_UCSC = make_array("47 students","4 students", "915 students", "703 students", "939 students")

UCSC_GRADUATION = Table().with_columns(
    "Race", Race,
    "Grad Demographics by Percentage", Grad_Percentage_UCSC,
    "Grad Demographic Count", Grad_Count_UCSC)
UCSC_GRADUATION


# In[152]:


#UC MERCED DEMOGRAPHICS 

Campus_Percentage_UCM = make_array("4.4%", "0.08%", "55.5%", "19%","8.9%")
Campus_Count_UCM = make_array("361 students", "7 students", "4,526 students", "1,550 students", "729 students")

UCM_CAMPUS_DEMOGRAPHICS = Table().with_columns(
   "Race", Race,
   "Campus Demographics by Percentage", Campus_Percentage_UCM,
   "Campus Demographic Count", Campus_Count_UCM)
UCM_CAMPUS_DEMOGRAPHICS


# In[185]:


#UC MERCED GRADUATION STATS

Grad_Percentage_UCM = make_array("6.4%", "0.2%", "44.3%", "25.6%", "14.5%")
Grad_Count_UCM = make_array("64 students", "2 studnets", "437 students", "253 students", "143 students")

UCM_Grad_Stats = Table().with_columns(
    "Race", Race,
    "Grad Demographics by Percentage", Grad_Percentage_UCM,
    "Grad Demographic Count", Grad_Count_UCM)
UCM_Grad_Stats


# In[133]:


#UC DAVIS DEMOGRAPHICS 

Campus_Percentage_Davis = make_array("3.7%", "0.5%", "22.6%", "31.6%", "22.8")
Campus_Count_Davis = make_array("1,101 students", "185 students", "6,715 students", "9,568 students", "7,178 students")
Davis_CAMPUS_DEMOGRAPHICS = Table().with_columns(
    "Race", Race,
    "Campus Demographics by Percentage", Campus_Percentage_Davis,
    "Campus Demographic Count", Campus_Count_Davis)
Davis_CAMPUS_DEMOGRAPHICS


# In[141]:


#UC DAVIS GRADUATION STATS

Grad_Percentage_Davis = make_array("1.85%", "0.08%","15.8%", "38.6%", "30.7%")
Grad_Count_Davis = make_array("83 students","4 students", "708 students", "1,728 students", "1,374 students")

Davis_GRADUATION = Table().with_columns(
    "Race", Race,
    "Grad Demographics by Percentage", Grad_Percentage_Davis,
    "Grad Demographic Count", Grad_Count_Davis)
Davis_GRADUATION


# In[153]:


#UCSB DEMOGRAPHICS 

Campus_Percentage_UCSB = make_array("4.1%", "0.9%", "24.1%", "23.9%", "29.9%")
Campus_Count_UCSB = make_array("966 students", "201 students", "5,632 students", "5,575 students", "6,987 students")

UCSB_CAMPUS_DEMOGRAPHICS = Table().with_columns(
    "Race", Race,
    "Campus Demographics by Percentage", Campus_Percentage_UCSB,
    "Campus Demographic Count", Campus_Count_UCSB)
UCSB_CAMPUS_DEMOGRAPHICS


# In[154]:


#UCSB GRADUATION STATS
Grad_Percentage_UCSB = make_array("1.9%", "0.15%","23.8%", "22.7%", "38.4%")
Grad_Count_UCSB = make_array("74 students","6 students", "923 students", "879 students", "1,488 students")

UCSB_GRADUATION = Table().with_columns(
    "Race", Race,
    "Grad Demographics by Percentage", Grad_Percentage_UCSB,
    "Grad Demographic Count", Grad_Count_UCSB)
UCSB_GRADUATION


# In[135]:


#UCR DEMOGRAPHICS

Campus_Percentage_UCR = make_array("5.7%", "0.1%", "39.9%", "36.8%", "11.7%")
Campus_Count_UCR = make_array("1,264 students", "27 students", "8,804 students", "8,127 students", "2,576 students")

UCR_CAMPUS_DEMOGRAPHICS = Table().with_columns(
    "Race", Race,
    "Campus Demographics by Percentage", Campus_Percentage_UCR,
    "Campus Demographic Count", Campus_Count_UCR)
UCR_CAMPUS_DEMOGRAPHICS


# In[156]:


#UCR GRADUATION STATS 
Grad_Percentage_UCR = make_array("4.19%", "0.03%","37.1%", "39.1%", "11.6%")
Grad_Count_UCR = make_array("125 students","1 students", "1,107 students", "1,165 students", "347 students")

UCR_GRADUATION = Table().with_columns(
    "Race", Race,
    "Grad Demographics by Percentage", Grad_Percentage_UCR,
    "Grad Demographic Count", Grad_Count_UCR)
UCR_GRADUATION

#Source: https://www.univstats.com/colleges/university-of-california-riverside/graduation-rate/


# In[136]:


#UCI DEMOGRAPHICS
Campus_Percentage_UCI = make_array("3.3%", "0.2%", "25%", "39.2", "13.3%")
Campus_Count_UCI = make_array("1,004 students", "73 students", "7,582 students", "11,910 students", "4,036 students")

UCI_CAMPUS_DEMOGRAPHICS = Table().with_columns(
    "Race", Race,
    "Campus Demographics by Percentage", Campus_Percentage_UCI,
    "Campus Demographic Count", Campus_Count_UCI)
UCI_CAMPUS_DEMOGRAPHICS


# In[140]:


#UCI GRADUATION STATS
Grad_Percentage_UCI = make_array("1.8%", "0.07%","22.2%", "47.8%", "12.2%")
Grad_Count_UCI = make_array("76 students","3 students", "938 students", "2,019 students", "519 students")

UCI_GRADUATION = Table().with_columns(
    "Race", Race,
    "Grad Demographics by Percentage", Grad_Percentage_UCI,
    "Grad Demographic Count", Grad_Count_UCI)
UCI_GRADUATION


# In[157]:


#UCSD DEMOGRAPHICS 
Campus_Percentage_UCSD = make_array("2.8%", "0.4%", "21.2%", "36.5%", "19.3%")
Campus_Count_UCSD = make_array("877 students", "119 students", "6,526 students", "11,244 students", "5,933 students")

UCI_CAMPUS_DEMOGRAPHICS = Table().with_columns(
    "Race", Race,
    "Campus Demographics by Percentage", Campus_Percentage_UCSD,
    "Campus Demographic Count", Campus_Count_UCSD)
UCI_CAMPUS_DEMOGRAPHICS


# In[158]:


#UCSD GRADUATION STATS

Grad_Percentage_UCSD = make_array("2%", "0.3%","11.9%", "49%", "20.5%")
Grad_Count_UCSD = make_array("79 students","12 students", "469 students", "1,925 students", "809 students")

UCSD_GRADUATION = Table().with_columns(
    "Race", Race,
    "Grad Demographics by Percentage", Grad_Percentage_UCSD,
    "Grad Demographic Count", Grad_Count_UCSD)
UCSD_GRADUATION


# # Conclusion 
# 
# Every school in the UC Sytem has the consistant problem of not admitting enough Black and Native students. Some also have issues with Latinx students but for the most part latinx make up 24% of all students in the UC. It was clear that the top UCs has more issues with diversity then the lower ranking UCs. The lower ranking UCs had more minority students attending and earning degrees. Though there is still a decline in demographics for latinx students at UCM even though they are the majority. This may be an indicator of low retention rates. Overall the UC system still needs a lot of work to do. They may have diverse rates for Latinx, Asian, and White students but they are neglecting Black and Native American students. 

# In[ ]:




