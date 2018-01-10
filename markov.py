"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_string = open(file_path).read()
    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if i >= len(words) - 2:
            chains[bigram] = []
        else:
            if bigram not in chains:
                chains[bigram] = [words[i + 2]]
            else:
                chains[bigram].append(words[i + 2])
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    first_key = choice(chains.keys())
    words.extend(list(first_key))
    rand_value = choice(chains[first_key])
    words.append(rand_value)

    i = 1
    while True:
        new_key = (words[i], words[i + 1])
        if chains[new_key] == []:
            break
        else:
            rand_value = choice(chains[new_key])
            words.append(rand_value)
            i += 1

    # words.append(rand_value)
    # link = (first_key[1], rand_value)
    # rand_value_2 = choice(chains[link])

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
