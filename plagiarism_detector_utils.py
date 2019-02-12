"""
This module is a utility class for plagiarism_detector.py
Contains the plagiarism algorithm and helper methods that process input files and creates n-tuples
"""

import re


def calculate_plagarism(synonyms_dict, n_tuples_1, n_tuples_2):
    """
    Calculates the percent of n-tuples from n_tuples_1 that appear in n_tuples_2
    :param synonyms_dict: dictionary; {word : list of synonyms} formatted as {string : list}
    :param n_tuples_1: list; List of lists of n words from input file 1
    :param n_tuples_2: list; List of lists of n words from input file 2
    :return: float; between 0 and 1
    """
    count = 0
    for n_1 in n_tuples_1:
        for n_2 in n_tuples_2:
            if is_synonymous_tuple(synonyms_dict, n_1, n_2):
                count += 1
    return float(count) / len(n_tuples_2)


def is_synonymous_tuple(synonyms_dict, n_tuple_1, n_tuple_2):
    """
    Checks if each word in position i in respective tuples are the same
    or corresponds to each other in synonyms_dict
    :param synonyms_dict: dictionary; {word : list of synonyms} formatted as {string : list}
    :param n_tuple_1: tuple
    :param n_tuple_2: tuple
    :return: bool; True if tuples are synonymous else False
    """
    if len(n_tuple_1) != len(n_tuple_2):
        return False

    for i, _ in enumerate(n_tuple_1):
        n1_word, n2_word = n_tuple_1[i], n_tuple_2[i]
        if n1_word != n2_word:
            if n1_word not in synonyms_dict:
                return False

            n1_word_synonyms = synonyms_dict[n1_word]

            if n2_word not in n1_word_synonyms:
                return False
    return True


def process_synonyms(synonyms_file):
    """
    Reads through synonyms_file and generates a dictionary of words and their synonyms
    :param synonyms_file: string; path location of the synonyms file
    :return: dictionary; {word : list of synonyms} formatted as {string : list}
    """
    try:
        synonyms_dict = {}
        regex = r'\b([a-z]+)\b'  # only get the words from the input file
        with open(synonyms_file) as file:
            for line in file:
                # Assumes each line has words that are synonyms with other words on that line
                words = re.findall(regex, line)
                for word in words:
                    synonyms_dict[word] = words

        return synonyms_dict

    except:
        raise FileNotFoundError("File does not exist or is not valid")


def process_input_file(input_file, n_tuple_size=3):
    """
    Reads and parses input file into a list of n-tuples of words
    :param input_file: string; Path location to input file
    :param n_tuple_size: int; size of n-tuples, default is 3
    :return: list; lists of n-tuples
    """
    try:
        words = []
        regex = r'\b([a-z]+)\b' # only get the words from the input file
        with open(input_file) as file:
            for line in file:
                words_on_line = re.findall(regex, line)
                words.extend(words_on_line)

        n_tuples = create_n_tuples(words, n_tuple_size)
        return n_tuples

    except:
        raise FileNotFoundError("File does not exist or is not properly formatted")


def create_n_tuples(words, n_tuple_size=3):
    """
    Given a list of words, creates a list of lists of n words
    :param words: list; list of words from input file
    :param n_tuple_size: int; determines size of inner lists
    :return: list; list of lists of n words
    """

    if len(words) < n_tuple_size:
        return words

    n_tuples = []
    for i in range(len(words) - n_tuple_size + 1):
        n_tuple = []
        for j in range(i, i + n_tuple_size):
            n_tuple.append(words[j])

        n_tuples.append(n_tuple)

    return n_tuples
