#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:52:26 2020

@author: msuherma
"""
# Exercise 1-2 using Python as a calculator

# --------------------------------------------

# 1
m= 60 # 1 minute =60 seconds
# ? How many seconds are there in 42 minutes 42 seconds
# SOLUTION #1
40*60+42    # or can be done by
40*m+42
#ANSWER No.1 is 2562

# --------------------------------------------

# 2
# How many miles are there in 10 km?
ml=1.61 #1 ml= 1.61 km
#SOLUTION #2
10/ml #or can be done by
10/1.61
#ANSWER No.2 is 6.21118.... 

# --------------------------------------------
# 3
# Tom runs 10 km in 42 minutes 42 seconds; determine the pace (min/mile) & sec/mile and avg.speed (mile/hr)
hr= 3600 # 1 hr = 3600 seconds
# 3.a.1 Pace min/mile
(42+42/60)/6.21118
#ANSWER 3.a.1 6.8747 min/mile
    # 3.a.2 Pace sec/mile
(42*60+42)/6.21118
#ANSWER 3.a.2 is 412.482 sec/mile
#or can be done
6.8747*60   # the answer is the same = 412.482

# 3.b average speed (mile/hr)
6.21118/((42+42/60)/60) # 60 denominator in the last is 1 min =1/60 hr
#ANSWER is 8.72765... mile/hr