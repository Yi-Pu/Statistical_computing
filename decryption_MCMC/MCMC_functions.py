# This scrip is to define functions needed to run MCMC

import numpy as np
import random
import string
import math

# Set seed for random number
random.seed(111111)

# Load reference text
with open(
    'ref2.txt',
        'r') as reference:
    reference_text = reference.read().replace('\n', '')

# Get the list of alphabet
# Get the list of alphabet
alphabet = string.ascii_lowercase
list_alphabet = list(alphabet)
alphabet_list = list_alphabet


def cipher_string(cipher):
    '''This function can convert a cipher
    dictionary to a string'''

    cipher_st = ''
    for key in alphabet:
        if key in cipher:
            cipher_st = cipher_st + cipher[key]
    return cipher_st


def string_cipher(in_string):
    '''This function can convert a string
    to a cipher dictionary'''

    cipher = {}
    for i in range(len(in_string)):
        cipher[list_alphabet[i]] = in_string[i]
    return cipher


def apply_cipher(text, ci):
    '''This function can encrypt/decrypt a text
    using a given cipher dictionary'''

    text = list(text)
    new_text = ''
    for char in text:
        if char.lower() in ci:
            new_text += ci[char.lower()]
        else:
            new_text += char
    return new_text


def create_single_count_dict(text):
    '''This function will pre-process the text
    and count single characters in a given text'''

    single_count = {}
    data = list(text.strip())
    for i in range(len(data) - 1):
        char = data[i].lower()

        # Change special characters to spaces
        if char not in alphabet_list and char != " ":
            char = " "

        # Count single characters
        if char in single_count:
            single_count[char] += 1
        else:
            single_count[char] = 1

    return single_count


def create_pair_count_dict(text):
    '''This function will pre-process the text
    and count character pairs in a given text'''

    pair_count = {}
    data = list(text.strip())
    for i in range(len(data) - 1):
        char_1 = data[i].lower()
        char_2 = data[i + 1].lower()
        key = char_1 + char_2

        # Change special characters to spaces
        if char_1 not in alphabet_list and char_1 != " ":
            char_1 = " "
        if char_2 not in alphabet_list and char_2 != " ":
            char_2 = " "

        # Count character pairs
        if key in pair_count:
            pair_count[key] += 1
        else:
            pair_count[key] = 1

    return pair_count


def create_pair_frequency_dict(text):
    '''This function will calculate the log frequency
    that a certain pair appears. For instance, 'a' appears
    for n times, and 'ab' appears for m times. Then the
    frequency that 'ab' appears is m/n.'''

    frequency_dict = {}
    text_pair = create_pair_count_dict(text)
    text_single = create_single_count_dict(text)
    for i in range(len(list(text_pair.keys())) - 1):
        key = list(text_pair.keys())[i]
        if key[0] in text_single:
            frequency_dict[key] = text_pair[key]/text_single[key[0]]
    return frequency_dict


def create_pair_log_frequency_dict(text):
    '''This function will calculate the log frequency
    that a certain pair appears. For instance, 'a' appears
    for n times, and 'ab' appears for m times. Then the
    frequency that 'ab' appears is m/n. And its log
    frequency is log(m)-log(n)'''

    frequency_dict = {}
    text_pair = create_pair_count_dict(text)
    text_single = create_single_count_dict(text)
    for i in range(len(list(text_pair.keys())) - 1):
        key = list(text_pair.keys())[i]
        if key[0] in text_single:

            frequency_dict[key] = math.log(text_pair[key]) - \
                math.log(text_single[key[0]])
    return frequency_dict


# Get the frequency dictionaty of character pairs from reference text
reference_pair = create_pair_frequency_dict(reference_text)
# Get the log frequency dictionaty of character pairs from reference text
likelihood_table = create_pair_log_frequency_dict(reference_text)


def get_cipher_log_likelihood(text, in_cipher):
    '''This function calculated the log likelihood
    of certain text given a cipher'''

    # Decrypt text using given invert cipher dictionary
    decrypted_text = apply_cipher(text, in_cipher)

    # Set initial log likelihood
    likelihood = 0

    for i in range(len(decrypted_text)-1):
        char_1 = decrypted_text[i]
        char_2 = decrypted_text[i + 1]
        key = char_1 + char_2
        if key in likelihood_table:
            likelihood = likelihood + likelihood_table[key]
        else:
            '''Things which do not appear in our reference
            text should have probability 0, so we want to
            put log(0) = -infinity here. Setting this equal
            to -25 is good enough'''
            likelihood = likelihood - 25

    return likelihood


def generate_swap(cipher):
    '''
    Swap cipher. This will move from current cipher
    d to next cipher d'
    '''
    pos1 = random.randint(0, len(list(cipher)) - 1)
    pos2 = random.randint(0, len(list(cipher)) - 1)
    if pos1 == pos2:
        return generate_swap(cipher)
    else:
        cipher = list(cipher)
        pos1_alpha = cipher[pos1]
        pos2_alpha = cipher[pos2]
        cipher[pos1] = pos2_alpha
        cipher[pos2] = pos1_alpha
        return "".join(cipher)


def MCMC_sample_cipher(text, steps):
    '''This function if to using the functions
    defined above to implement MCMC algorithm'''
    current_cipher_st = string.ascii_lowercase

    # Set initial parameters
    best_state = ''
    switched = 0
    score = -1000000

    for i in range(steps):
        # Genearate new cipher
        proposed_cipher_st = generate_swap(current_cipher_st)
        current_cipher = string_cipher(current_cipher_st)
        proposed_cipher = string_cipher(proposed_cipher_st)

        # Calculate liklihood
        score_current_cipher = get_cipher_log_likelihood(text, current_cipher)
        score_proposed_cipher = get_cipher_log_likelihood(
            text, proposed_cipher)

        # Generate U(0, 1) and compare
        if math.log(np.random.uniform(low=0, high=1, size=1)) <  \
                (score_proposed_cipher - score_current_cipher)*1.5:
            current_cipher_st = proposed_cipher_st
            switched += 1

        # print out current iteration times and steps already taken
        if i % 500 == 0:
            print(
                'Iteration ' + str(i) + ', step ' + str(switched) +
                ' of the chain: ' +
                apply_cipher(text, current_cipher)[0:100] + '...')

        # Keep notes of the maximum L(d)
        if score_current_cipher > score:
            best_state = current_cipher_st
            score = score_current_cipher

    return best_state
