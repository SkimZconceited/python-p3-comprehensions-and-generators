#!/usr/bin/env python3

def return_evens(num_list):
    result = []
    [result.append(num) for num in num_list if num % 2 == 0]
    print(result)
    return result
    pass
return_evens(range(1, 10, 2))
return_evens([0, 1, 3, 5, 7, 8, 9])


def make_exclamation(sentence_list):
    result = []
    [result.append(sentence + '!') for sentence in sentence_list]
    return result if sentence_list == True else result
    print(result)
    # pass
make_exclamation(["Hello", "I'm doing great", "Python is fun"])