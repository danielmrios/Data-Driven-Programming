# -*- coding: utf-8 -*-
"""Practice_problem_8

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17dL_y5whvT1HLBs8I8L7IfBk5ofUpim2
"""

import random
def guess_game(upper_limit, m):
  '''
  @file name: Guessing_game
  @group: Team 8
  @authors: Adil Shafqat, Qianxun Tu, Adil Shafqat
  @description: The program plays a guessing game with the user by randomly
  selecting a number between 1 and a given upper limit, then the user has
  m amount of chances to guess the number.
  @date created: 10/9/2023
  @version: 1.00
  '''
  target = random.randint(1, upper_limit)
  guesses = []

  print(f'Guess a number between 1 and {upper_limit}. You have {m} guesses.')
  for attempt in range(m):
    guess = input('Guess a number or quit: ')
#User inputs a number or quit
    if guess.lower() == 'quit':
      #If the user says quit, the game ends and they lose
      print('Game is over')
      return guesses
    #If the user puts a different input other than an integer or quit,
    #the program says invalid input
    try:
      guess = int(guess)
    except ValueError:
      print('Invalid input. Enter a number or quit.')
      continue

    guesses.append(guess)
    if guess == target:
      if attempt < m // 3:
        print('Excellent')
        #if the user guesses within m//3 guesses, they get an excellent score
      elif m // 3 <= attempt < 2 * m // 3:
        #if the user guesses within 2m//3 or m//3 guesses, they get a pretty good score
        print('Pretty good')
        #if the user takes over 2m//3 guesses, they get an OK score
      else:
        print('OK')
        #the program produces all guesses made by the user
      return guesses
      #if the guess is below the target value, the program says it's too low
    elif guess < target:
      print('Too low, keep trying')
      #if the guess is above the target value, the program says it's too high
    else:
      print('Too high, keep trying')
  print('Game over')
  return guesses
guess_game(150, 10)