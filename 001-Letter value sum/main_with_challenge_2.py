import os
def get_sum(word:str) -> int:
    values:list = []
    value:int
    for i in word:
        value = ord(i) - 96 # -96 because in the ascii, letters start at 97.
        values.append(value)
    return sum(values)

def get_word_length(word:str) -> int:
    return len(word)

with open("001-Letter value sum/enable1.txt","r") as file:
    file_raw:str = file.read()
    file_split:list = file_raw.split("\n")
    word_length:int
    word_sum:int
    odd:int = 0
    for p in file_split:
        word_length = get_word_length(p)
        word_sum = get_sum(p)
        if word_length % 2 != 0:
            odd += 1
        