# -*- coding: utf-8 -*-
"""PracProb_13

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CJAsiygAgmSaLiD2IUPVXXMhffAz-f7N
"""

from google.colab import drive
drive.mount('/content/drive')

'''
@filename: PracProb_13.py
@team: Team 8
@authors: Adil Shafqat, Qianxun Tu, Daniel Rios
@description: The program reads a file election.csv,
cleans it, then writes in a created text file the
results of the election state-by-state, as well as
the percentage margin for the winning party.
@datecreated: 10/25/23
@version: 1.00
'''
file_path = '/content/drive/My Drive/election.csv'
election_file = open(file_path, 'r')

#Delete first 4 lines (headings) of file
for i in range(4):
  election_file.readline()

#Create text file named winners.txt in google drive
#output results into created file
output_file_path = '/content/drive/My Drive/winner.txt'
out_file = open(output_file_path, 'w')

#split data from election.csv by commas
for j in election_file:
  j = j.replace('%', '')
  data = j.split(',')

#Assign variables to position in data file
#namely state name, total democratic votes,
#total republican votes, and the percent of votes
#that were democratic or republican
  state_name = data[0]
  democratic_votes = int(data[2])
  democrat_percent = float(data[3])
  republican_votes = int(data[5])
  republican_percent = float(data[6])
#Decide the winning party for each state in the file
  if democratic_votes > republican_votes:
    winner = 'Democratic'
  else:
    winner = 'Republican'
#Calculate the percentage difference between the parties
  percent_diff = abs(republican_percent - democrat_percent)
#write the calculated data in the file
  out_file.write(f'{state_name} {winner} {percent_diff:.2f}%\n')

#close the text file and election file
election_file.close()
out_file.close()
#Look at the content of the file in the program as well
text_file = open('/content/drive/My Drive/winner.txt')
for line in text_file:
  print(line)