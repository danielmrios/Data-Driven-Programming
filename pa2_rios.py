# -*- coding: utf-8 -*-
"""PA2-Rios.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z7GMl0AU6WZgFMPkg1__WSuDO8GNcXHy
"""

from google.colab import files
uploaded = files.upload()

'''
@filename: PA2-Rios.py
@authors: Daniel Rios
@description: The code reads a DNA sequence from a file. It then defines a
function, mostCommonK, which takes a DNA sequence and a specific
k value length as input and determines the most common k-letter substring within
the sequence. The function returns the highest count of occurrences and the
corresponding substring. The final program provides the most common k-letter
substrings for a range of k values.
@date: 10/30/23
@version: 1.0
'''

# open the file and read its content into 'dna'
my_file = open('initial6000.txt')
dna = my_file.read()
# assign the filename to call for later use
filename = 'initial6000.txt'

# define a function to find the most common k-letter substring in a DNA sequence
def mostCommonK(dna, k):
  #iInitialize variables highest count and the corresponding target substring
    highestCount = 0
    targetWithHighestCount = ""

  # iterate through the DNA sequence to explore possible substrings
    for i in range(len(dna) - k + 1):
        target = dna[i:i + k]
        # reset count for the current target
        count = 0

        # compare the target with other substrings in the DNA sequence
        for j in range(len(dna) - k + 1):
            if dna[j:j + k] == target:
                count += 1

        # update if a higher count is found
        if count > highestCount:
            highestCount = count
            targetWithHighestCount = target

    # return the target substring with the highest count
    return highestCount, targetWithHighestCount

# define a function to find the most common substring within a given length range
def mostCommonSubstring(dna, min_length, max_length):
    # initialize variables to keep track of the substring with the highest count
    # and the corresponding best 'k' value
    highestCount = 0
    best_k = 0

    # iterate through k values within range
    for k in range(min_length, max_length + 1):
        count, _ = mostCommonK(dna, k)
        # update the highest count and the best k value if a higher count is found
        if count > highestCount:
            highestCount = count
            best_k = k

    # return the best k value and the highest count
    return best_k, highestCount

# define a function to run the mostCommonSubstring on given parameters
def runMostCommonSubstring(filename, min_length, max_length):
    # open the file for reading
    with open(filename, 'r') as file:
        dna = file.read()

    # call the function to find the best k valye and the highest count
    best_k, highest_count = mostCommonSubstring(dna, min_length, max_length)

    # print the results

    print(f"Data file: {filename}")
    print(f"mink: {min_length}")
    print(f"maxk: {max_length}")
    print(f"mostCommonSubstring(dna, {min_length}, {max_length}) = '{mostCommonK(dna, best_k)[1]}', {highest_count}")

# call the runMostCommnSubstring function with test values
runMostCommonSubstring(filename, 4, 9)
print()
runMostCommonSubstring(filename, 3, 6)
print()
runMostCommonSubstring(filename, 5, 10)