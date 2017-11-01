# _*_coding:utf-8_*_

#！/usr/local/bin/python    MAC
# filename:exercise25.py

#intend :what is def.and method

def break_words(stuff):
    """This function will break up words for us."""
    # result：['This', 'function', 'will', 'break', 'up', 'words', 'for', 'us.']
    words = stuff.split(' ')
    return words
def sort_words(words):
    """Sorts the words."""
    # result：[' ', ' ', '.', 'S', 'd', 'e', 'h', 'o', 'o', 'r', 'r', 's', 's', 't', 't', 'w']
    return sorted(words)
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # result :['Takes', 'a', 'and', 'full', 'in', 'returns', 'sentence', 'sorted', 'the', 'words.']
    words = break_words(sentence)
    return sort_words(words)
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)

    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)



print break_words("""This function will break up words for us.""")
print sort_words("""Sorts the words.""")
listargv = ['Prints', 'the', 'first', 'word', 'after', 'popping', 'it', 'off.']
print_first_word(listargv)
print_last_word(listargv)
print sort_sentence("""Takes in a full sentence and returns the sorted words.""")
print_first_and_last("""Prints the first and last words of the sentence.""")
print_first_and_last_sorted("""Sorts the words then prints the first and last one.""")
