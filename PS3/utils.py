import random

def is_valid_word_without_wildcard(word, hand, word_list):
    in_wordlist = check_wordlist(word, word_list)
    result = copy_map(hand)
    for char in word:
        if result.get(char, 0) > 0:
            result[char] -= 1
        else:
            return False    
    if not in_wordlist:
        return False    
    return True


def is_valid_word_with_wildcard(word, hand, word_list):
    possible_wordslist = []
    i = word.find("*")
    for x in word_list:
        first = word[0 : i]
        last = word[i + 1:]
        if ((first in x[0 : i] and last in x[i + 1: ]) and 
            (len(first) + len(last) + 1 == len(x)) and 
            (x[i] not in "bcdfghjklmnpqrstvwxyz")):
            possible_wordslist.append(x)
    if len(possible_wordslist) > 0:
        return True
    return False


def get_substitute(hand, letter):
    alphabet = "bcdfghjklmnpqrstvwxyz*aeiou"
    sub = random.choice(alphabet)
    while sub != letter and sub not in hand.keys():
        return random.choice(sub)
    return get_substitute(hand, letter)


def comp_1(word):
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    comp1 = []
    for k, v in SCRABBLE_LETTER_VALUES.items():
        for x in word:
            if x == k:
                comp1.append(v)
    return sum(comp1)


def comp_2(word, n):
    length = len(word)
    exp = 7 * length - 3 * (n - length)
    if (exp < 1):
        comp2 = 1
    else:
        comp2 = exp
    return comp2


def updated_hand(hand, word):
    result = copy_map(hand)
    for char in word:
        if char in result:
            result[char] -= 1
        else:
            result[char] = 0
    if result.get(char, 0) < 1:
        return clean_hand(result)
    return clean_hand(result)


def copy_map(map):
    result = {}
    for k, v in map.items():
        result[k] = v
    return result


def check_wordlist(word, word_list):
    if word in word_list:
        return True
    return False

    
def clean_hand(hand):
    result = {}
    for k, v in hand.items():
        if v > 0:
            result[k] = v
    return result         