# Author: Samuel Bennett
# Date: 5/19/2021
# Description: Function determines what words are the same in two strings
def words_in_both(w1, w2):
    sent1 = w1.lower().split(" ")
    sent2 = w2.lower().split(" ")
    result = []
    for x in sent1:
        if (x in sent2) and (x not in result):
            result.append(x)
    return result

print(words_in_both("There once was a man from Nantucket", "There once was a old man named Jankins"))