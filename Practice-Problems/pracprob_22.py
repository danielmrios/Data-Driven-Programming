# -*- coding: utf-8 -*-
"""PracProb_22.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rp4-7PTdg4KJYvwmbKvGst_gIQYp-vWF
"""

'''
@filename: PracProb_22.py
@authors: Adil Shafqat, Qianxun Tu, Daniel Rios
@description: the program uses a class Footage which takes
feet and inches as an argument. It can add or substract two heights,
as well as compare them by outputting true or false if one of the
heights is larger or smaller than the other
@date: 11/27/2023
@version: 1.00
'''
#define class
class Footage:
#initialize variables
  def __init__(self, feet, inches):
    self.feet = feet
    self.inches = inches
#string function that prints height in feet and inches
  def __str__(self):
    return f"{self.feet}' {self.inches}\""

#add function that adds heights together. Accounts for if
#inches is larger than 12, it adds 1 to feet and takes 12 away
#from inches
  def __add__(self, other):
    total_feet = self.feet + other.feet
    total_inches = self.inches + other.inches
    if total_inches >= 12:
      total_feet += 1
      total_inches -= 12
    return Footage(total_feet, total_inches)

#substract function that substracts heights from each other. Also
#accounts for same case in add function
  def __sub__(self, other):
    total_feet = self.feet - other.feet
    total_inches = self.inches - other.inches
    if total_inches < 0:
      total_feet -=1
      total_inches += 12
    return Footage(total_feet, total_inches)

#greater than function that sees if one height is greater
#than another height
  def __gt__(self, other):
    if self.feet > other.feet:
      return True
    elif self.feet == other.feet and self.inches > other.inches:
      return True
    else:
      return False

#less than function that sees if one height is less than
#another height
  def __lt__(self, other):
    if self.feet < other.feet:
      return True
    elif self.feet == other.feet and self.inches < other.inches:
      return True
    else:
      return False

#various calls for each function
F1 = Footage(10, 9)
F2 = Footage(1, 8)

print(F1 + F2)
print(F1 - F2)
print(F1 > F2)
print(F1 < F2)