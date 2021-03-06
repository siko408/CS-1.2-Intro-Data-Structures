#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
from histogram import *
import random
from random import choice


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        self.copy_list = word_filter(word_list.copy())
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        if word in self:
            self.tokens += count
            value = self.get(word)
            value += count
            self.update({word: value})
        else:
            self.update({word: count})
            self.types += 1
            self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        for word2 in self:
            if word2 == word:
                return self[word]
        return 0

    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        total = sum(self.values())  # Getting all values
        result = random.randint(1, total)  # Random value from 1 to totalValues
        for word in self:
            if result - self[word] <= 0:
                return word
            result -= self[word]

    def mokov_chain(self, chosen_word):
        """ Creating a mokup of the histogram """
        temp_dict = {}
        for index in range(len(self.copy_list)):
            if self.copy_list[index].lower() == chosen_word.lower() and index < len(self.copy_list)-1:
                if self.copy_list[index + 1] not in temp_dict:
                    temp_dict.update({self.copy_list[index + 1]: 1})
                else:
                    value = temp_dict.get(self.copy_list[index + 1])
                    value += 1  # Increase the findings by one
                    temp_dict.update({self.copy_list[index + 1]: value})
        #  Get word frequency for closest words
        max_value = 0
        chance = []
        for val in temp_dict.values():
            if max_value < val:
                max_value = val
        for key in temp_dict.keys():
            value = temp_dict.get(key)
            if max_value == value:
                chance.append(key)  # Append word with the maximum value
        if len(chance) == 1:
            return chance[0]
        elif len(chance) > 1:
            return chance[random.randint(0, len(chance)-1)]
        else:
            return self.copy_list[random.randint(0, len(self.copy_list)-1)]
    # TODO: Randomly choose a word based on its frequency in this histogram

    def markov_chain_v2(self, chosen_word):
        """ Creating a mokup of the histogram n state """
        stateDict = {}
        startingState = word_filter(chosen_word)  # Split the words
        for index in range(len(self.copy_list)):
            wordState = word_filter(self.copy_list[index: len(startingState)])  # Returns a list of words
            if startingState == wordState and index < len(self.copy_list)-1:
                if
    # TODO: Randomly choose a word based on its frequency in this histogram


def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    #  print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]  # change the range back to 10000
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        #  print_histogram(arguments)
        histogram = Dictogram(text)
        chosen_word = histogram.sample()  # Pick a random word based on percentage
        chain = [chosen_word]
        for _ in range(20):
            chosen_word = histogram.mokov_chain(chosen_word)
            histogram.mokov_chain(chosen_word)
            chain.append(chosen_word)
        print(chain)
    else:
        histogram = Dictogram(getText().split())
        chosen_word =  "rat-faced"  #  histogram.sample()  # Pick a random word based on percentage
        chain = [chosen_word]
        for _ in range(10):
            chosen_word = histogram.mokov_chain(chosen_word)
            chain.append(chosen_word)
        print(chain)


if __name__ == '__main__':
    main()
