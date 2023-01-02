# Your function implementation(s) should go here


# Defince a function to find anagrams from a given list of words
def find_anagrams(words):
    # Create a list to store anagrams
    anagrams = []

    # If the input is an empty list, raise error
    if not words:
        raise ValueError("the input is not valid")

    # Sort each word on the list
    sorted_words = [''.join(sorted(word.lower())) for word in words]

    # Build a dictionary where the key is each sorted word,
    # and value is a list of indices where each word is
    d = {}
    for i, sorted_word in enumerate(sorted_words):
        d.setdefault(sorted_word, []).append(i)

    # Traverse the dictionary and read indices for each sorted key.
    # Build a set for each sorted key, and combine all sets
    for index in d.values():
        collection = set(words[i] for i in index)
        if len(collection) > 0:
            anagrams.append(collection)

    return anagrams
