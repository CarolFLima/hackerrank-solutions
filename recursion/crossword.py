#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    
    class Word():
        def __init__(self, start_x, start_y, direction):
            self.start_x = start_x
            self.start_y = start_y
            self.direction = direction

        def set_len(self, len):
            self.len = len

    word_pool = []

    def create_word(i, j, direction):
        # print('Variaveis i: {}, j: {}, dir: {}'.format(i, j, direction))
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
    while not solved:
        curr_word = word_pool[pointer]

        if curr_word.direction == 'across':
            pass
        else:
            pass




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
