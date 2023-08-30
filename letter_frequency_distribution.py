#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

page = [i.split() for i in open("/home/lao_tzu/page-0")][0] ## LIBER PRIMUS 0.JPG (See Cicada 3301 Liber Primus Unsolved Pages)
page_string = ''.join(page)
page_len = len(page_string)
print(''.join(page))

distribution = {}

## CALCULATING LETTER FREQUENCIES

for character in alphabet:
    number = 0
    for char in page_string:
        if char == character:
            number += 1
    distribution[character] = number

## SORTING THE DISTRIBUTION DICTIONARY (PRINTING IT OUT IN DESCENDING ORDER)

sorted_values = sorted(distribution.values(), key=None, reverse=True)
sorted_distinct_values = sorted(list(set(sorted_values)), key=None, reverse=True)

for num in sorted_distinct_values:
    letter_matches = []  ## Stays empty as long as the number only appears once in the list
    if sorted_values.count(num) == 1:
        print(f'{list(distribution.keys())[list(distribution.values()).index(num)]} ----- {num/page_len}|{num}')
    else:
        for key in distribution.keys():
            if distribution[key] == num:
                letter_matches.append(key)
        for letter in sorted(letter_matches, key=None, reverse=True):
            print(f'{letter} ----- {num/page_len}|{num}')

letters = list(distribution.keys())
frequencies = list(distribution.values())

fig = plt.figure(figsize=(10, 5))
plt.bar(letters, frequencies, color="coral", width=0.4)
plt.xlabel("Letters in the English alphabet")
plt.ylabel("Usage frequency")
plt.title("Letter Frequency Distribution")
plt.show()
