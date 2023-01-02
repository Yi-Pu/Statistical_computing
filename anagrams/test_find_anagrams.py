# This is to test the find_anagrams function
from find_anagrams import find_anagrams
import pytest

# Regular values
test_words1 = [
    "cinema", "iceman", "dopiest",
    "deposit", "posited", "topside",
    "anagram", "doggerel"]
correct_answer1 = [
    {"cinema", "iceman"},
    {"dopiest", "deposit", "posited", "topside"},
    {"anagram"},
    {"doggerel"}
]
test_words2 = [
    "Abd", "bda", "abd",
    "cccv", "Vccc", "VCCC",
    "ka", "dl"]
correct_answer2 = [
    {"Abd", "bda", "abd"},
    {"cccv", "Vccc", "VCCC"},
    {"ka"},
    {"dl"}
]
# Edge values
test_words_3 = ["a"]
correct_answer_3 = [{"a"}]


def test_regular_values():
    # This function is to test whether the find_anagrams
    # function works correctly for normal values

    # Check if all factors are the same
    assert find_anagrams(test_words1) == correct_answer1
    assert find_anagrams(test_words2) == correct_answer2


def test_edge_values():
    # This function is to test whether the find_anagrams
    # function works correctly for edge values

    # Check if all factors are the same
    assert find_anagrams(test_words_3) == correct_answer_3


def test_errors():
    # This function is to test whether the find_anagrams
    # can raise error as expected

    # Test for empty list
    with pytest.raises(ValueError):
        find_anagrams([])
