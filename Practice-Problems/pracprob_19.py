# -*- coding: utf-8 -*-
"""PracProb_19

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yQLR_lHvvx_rSKJ7NhFGf3jq_YI6LsNf
"""

'''
@filename: PracProb_19.py
@authors: Adil Shafqat, Qianxun Tu, Daniel Rios
@description: The program creates lists of 1-100 for A, B, and C, first
without using numpy, and then with using numpy. It also creates a list D
which is the sum of corresponding values in A, B, C. The program loops for
4 seconds and increments the values in A, B, C by 1, while continously
summing and assigning the values to list D. It also has a running count of
the number of iterations. This is first done without using numpy, and then
with using nunmpy. The final numbers for D[0] and iterations with and without
numpy are compared
@date: 11/15/2023
@version: 1.00
'''
#Part 1(a):

import time
#create lists of 1-100 for A, B, C
A = list(range(1,101))
B = list(range(1,101))
C = list(range(1,101))
#create D as list of 100 zeroes
D_without = [0] * 100

#initialize start_time and iterations without numpy
start_time = time.time()
iterations_without = 0

#while loop until 4 seconds have passed
while time.time() - start_time < 4.0:
#increment A, B, and C using for loop
  for i in range(100):
    A[i] += 1
    B[i] += 1
    C[i] += 1
#assign D as sum of corresponding values in A, B, C
    D_without[i] = A[i] + B[i] + C[i]
#increment iterations by 1 for each iteration in loop
  iterations_without += 1

#print D[0] and number of iterations without using numpy
print(f'D[0] without numpy: {D_without[0]}')
print(f'Number of iterations without numpy: {iterations_without}')
print()


#Part 1(b):

import numpy as np
#create lists for A, B, C using built-in numpy functions
A = np.arange(1,101)
B = np.arange(1,101)
C = np.arange(1,101)
#create D as list of 100 zeroes
D_with = np.zeros(100)

#initialize start_time and iterations with numpy
start_time = time.time()
iterations_with = 0

#while loop until 4 seconds have passed
while time.time() - start_time < 4.0:
#increment A, B, C by 1 for each iteration
  A += 1
  B += 1
  C += 1
#assign D with the sum of A, B, C
  D_with = A + B + C
#increment iterations by 1 for each iteration in loop
  iterations_with += 1

#print D[0] and number of iterations using numpy
print(f'D[0] with numpy: {D_with[0]}')
print(f'Number of iterations with numpy: {iterations_with}')
print()

#compare D[0] with and without using numpy
if D_with[0] > D_without[0]:
  print(f'D[0] using numpy is larger by {D_with[0] - D_without[0]}')
else:
  print(f'D[0] without using numpy is larger by {D_without[0] - D_with [0]}')
#compare iterations with and without using numpy
if iterations_with > iterations_without:
  print(f'There are {iterations_with - iterations_without} more iterations using numpy')
else:
  print(f'There are {iterations_without - iterations_with} more iterations without using numpy')