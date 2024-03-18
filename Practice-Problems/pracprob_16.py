# -*- coding: utf-8 -*-
"""PracProb_16

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JebpUBz3UUn9L9qjM8do_MRJeSePU8u8
"""

from google.colab import drive
drive.mount('/content/drive')

my_file = open('/content/drive//MyDrive/name_age.csv')
def make_dictionary_names(file_name):
  name_dict = {}

  for row in my_file:
    row = row.replace('"', ' ')
    row = row.replace(' ', '')
    row = row.replace('\n', '')
    data = row.split(',')
    full_name = data[0] + ' ' + data[1]
    age = int(data[2])
    name_dict[full_name] = age
  print(name_dict)