# -*- coding: utf-8 -*-
"""PracProb_15

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FvLoWi8YBtYGt4rl0KrQtb6ISrhrUFZZ
"""

'''
@filename: PracProb_15.py
@authors: Adil Shafqat, Qianxun Tu, Daniel Rios
@description: the function asks the user to input a number between
1 and 99, then it converts it to an integer. The function then
iterates through the range till the input number, and outputs
a continual list of the correct suffix for each number, for
example 1st, 2nd, ..., 13th, ... 23rd, 24th etc.
@date: 10/30/23
@version: 1.00
'''
def iterations():
#function iterations asks user to input integer between 1 and 99
  while True:
    number = int(input("Enter an integer between 1 and 99: "))

#create dictionary of suffixes
    suffix = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th'}

#set range for number input by user to between 1 and 99
    if 1<= number <= 99:
#use for loop to iterate through entire range of numbers
      for i in range(1, number + 1):
#for special case of 11, 12, and 13, use 'th' as suffix,
#check this first as its a unique case
        if 11 <= i <= 13:
          suff = suffix[4]
#else if the remainder from dividing by 10 is 1, assign
#the suffix as 'st'. For example 21 is 21st
        elif i % 10 == 1:
          suff = suffix[1]
#else if the remainder from dividing by 10 is 2, assign
#the suffix as 'nd'. For example 22 is 22nd
        elif i % 10 == 2:
          suff = suffix[2]
#else if the remainder from dividing by 10 is 3, assign
#the suffix as 'rd'. For example 23 is 23rd
        elif i % 10 == 3:
          suff = suffix[3]
#else for all other numbers, assign the suffix as 'th'.
        else:
          suff = suffix[4]
#print the number and suffix, iterating through the
#entire range
        print(f"This is the {i}{suff} iteration")
iterations()