#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:19:22 2016

@author: chrisrappoli
"""

import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file by downloading the baseball_stats file from Downloadables below. 
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """

    filename = 'baseball_stats.csv'
    path = './data/'
    baseball_data = pandas.read_csv(path + filename)
    
    lefties = baseball_data[baseball_data['handedness'] == 'L']
    righties = baseball_data[baseball_data['handedness'] == 'R']
    
    result = scipy.stats.ttest_ind(lefties['avg'], righties['avg'], equal_var=False)
    
    if result[1] <= .05:
        return (False, result)
    else:
        return (True, result)
        
print(compare_averages('baseball_stats.csv'))