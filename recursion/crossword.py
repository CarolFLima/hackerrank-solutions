#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    
    words_arr = words.split(';')

    class Word():
        def __init__(self, start_x, start_y, direction):
            self.start_x = start_x
            self.start_y = start_y
            self.direction = direction

        def set_len(self, len):
            self.len = len
            print('Tamanho: {}'.format(len))

    word_pool = []

    def create_word(i, j, direction):
        word = Word(i, j, direction)

        counter_len = 0
        pointer = 0

        if direction == 'across':
            pointer = j
            while pointer < 10 and crossword[i][pointer] == '-':
                pointer += 1
                counter_len += 1
        else:
            pointer = i
            while pointer < 10 and crossword[pointer][j] == '-':
                pointer += 1
                counter_len += 1

        word.set_len(counter_len)
        word_pool.append(word)

    for i in range(10):
        for j in range(10):
            if crossword[i][j] == '-':
                if (i>0 and crossword[i-1][j] != '-') or i==0:
                    if i<9 and crossword[i+1][j] == '-':
                        create_word(i, j, 'down')
                if (j>0 and crossword[i][j-1] != '-') or j==0:
                    if j<9 and crossword[i][j+1] == '-':
                        create_word(i, j, 'across')
                

        # print('Tamanho da piscina de palavras  {}'.format(len(word_pool)))
    solved = False
    pointer = 0
    used_words = []

    def fill_word(pointer):
        i = 0
        while i < 4:
            curr_len = len(words_arr[i])
            if curr_len == word_pool[pointer].len and words_arr[i] not in used_words:
                break
            i += 1
        
        if  words_arr[i] not in used_words:
            used_words.append(words_arr[i])
       
    def remove_word():
        pass

        
    while not solved:
        fill_word(pointer)
        pointer += 1



        if pointer == len(words_arr):
            solved = True
        
    
    print('Used words: {}'.format(used_words))
    return crossword

if __name__ == '__main__':
    fptr = open('results.txt', 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
