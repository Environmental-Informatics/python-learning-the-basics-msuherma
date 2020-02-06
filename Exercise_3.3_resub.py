# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:39:57 2020

@author: msuherma@purdue.edu
"""
# Exercise 3.3
# PART 2 ~ Making 4x4 grid

plus_row = '+' + ' ' + 4 * ('-' + ' ')   # to make + started row
vert_row = '|' + 9 * ' '                 # to make | started row

def fcn_2x(f):       # to define a function that calls another function twice
    f()
    f()

def fcn_4x(f):        # to define a function that calls another function four times
    f()
    f()
    f()
    f()
    
                    
def print_4x1plus_grid():       #to create 4 column starting with '+' four '-' and spaces, ended with '+'
    print((4*plus_row) + '+')   #print 4 times plus row

def print_4x1vert_grid():       #to creat the columns with '|'
    print((4*vert_row) + '|')   #print 4 times of '|' column ended with '|'

# 4x4 vertical here means, each of column contains four | in vertical order
def print_4x4vert_grid():       #to make 4x4 vertical grid
    fcn_4x(print_4x1vert_grid)  #call function 4 times for 4x1 vertical grid

def print_4x1full_grid():       #to print full 4x1 grid, means 1 row starting with '+' and 4 rows starting with '|'       
    print_4x1plus_grid()        #4 columns 1 row of '+' starting grid
    print_4x4vert_grid()        #4 columns 4 row of '|' starting grid

def print_4x4full_grid():       #to print whole assigned grid, i.e. 4x4 grid
    fcn_4x(print_4x1full_grid)  #printing all 4x1 for four times
    print_4x1plus_grid()        #ended with '+' starting line

#print (print_4x4vert_grid())   #to clear the misunderstanding, 4x4 vertical grid meaning that it prints only '|' starting column 4 columns 4 row
print (print_4x4full_grid())      # to call the full 4x4 grid, if necessary

