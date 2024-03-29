# -*- coding: utf-8 -*-
"""PA1Rios.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xDqOiWHr5K9uKrp_4TXaBkoHmlsri_QQ
"""

'''
  @file name: Daniel Rios PA1
  @authors: Daniel Rios
  @date created: 10/11/2023
  @version: 1.00
  '''

def initials():
  # compose my initials
    print("XXXX    XXX")
    print("X   X   X  X")
    print("X    X  XXX")
    print("X    X  XX")
    print("X   X   X X")
    print("XXXX    X  X")


def futureValue(investment, interest_rate, years):
  # input investment values
  print(f'Enter Investment Amount: {investment}')
  print(f'Enter annual interest rate: {interest_rate}')
  print(f'Enter Number of Years: {years}')

  future_val_by_years = investment # initial investment
  # divide rate by 100 so it acts as a decimal
  yearly_rate = interest_rate / 100
  years_remaining = years

 # calculate yearly value using while loop and formula
  while years_remaining > 0:
    future_val_by_years *= (1 + yearly_rate)
    years_remaining -= 1

  # divide rate by 12 to get monthly interest rate
  monthly_interest_rate = yearly_rate / 12
  number_of_months = years * 12
  future_val_by_months = investment  # Initial investment
  months_remaining = number_of_months

# calculate monthly value using while loop and formula
  while months_remaining > 0:
      future_val_by_months *= (1 + monthly_interest_rate)
      months_remaining -= 1

  # calculate difference
  difference = future_val_by_months - future_val_by_years

  # print results
  print(f"Accumulated value (monthly) is ${future_val_by_months:.2f}")
  print(f"Accumulated value (yearly) is ${future_val_by_years:.2f}")
  print(f"Increase due to monthly compounding is ${difference:.2f}")

import math

def CoinArea(M, N):

  # input user coin values
  print(f'Enter number of dimes: {M}')
  print(f'Enter number of quarters: {N}')

  # convert diameter to radius and use in calculating area of dime
  dime_diameter = 17.9
  dime_radius = dime_diameter/2
  dime_area = M*((dime_radius)**2 * math.pi)

  # convert diameter to radius and use in calculating area of quarter
  quarter_diameter = 24.3
  quarter_radius = quarter_diameter/2
  quarter_area = N*((quarter_radius)**2 * math.pi)

  # calculate total area of dimes and quarters
  total_area = (dime_area + quarter_area)

  # calculate value of coins
  dime_value = M*0.1
  quarter_value = N*0.25
  total_value = (dime_value + quarter_value)

  # print area of dimes, quarters, total, and value of the coins
  print(f'The total area of {M} dimes is {dime_area: .2f} square millimeters')
  print(f'The total area of {N} quarters is {quarter_area: .2f} square millimeters')
  print(f'The total area of {M} dimes and {N} quarters is {total_area:.2f} square millimeters')
  print(f'The total value of the coins is ${total_value} dollars')

initials()

futureValue(1000, 3.25, 1)
futureValue(500, 5, 3)
futureValue(10000, 2.5, 5)

CoinArea(1, 1)
CoinArea(3, 5)
CoinArea(5, 10)
