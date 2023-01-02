# Your implementation of crowded_cows should go here


# Defince a function to find crowded cows
def crowded_cows(cows, k):
    # Raise error if the input is not valid
    if isinstance(k, int) is False:
        raise ValueError("k should be an integer")

    # Raise error if the input list is not valid
    if len(cows) == 0:
        raise ValueError("you should input a valid list of cows")

    # construct a dictionary where the key is the breed ID of a cow,
    # and value is a list of indices where the cow is
    d = {}
    for i, cow in enumerate(cows):
        d.setdefault(cow, []).append(i)

    # traverse the dictionary and
    # calculate the maximum distance within each breed
    # List of breed that's crowded
    crowded_breed = []
    for breed in d.keys():
        index_list = d[breed]
        dis = max(index_list) - min(index_list)
        if (dis <= k) & (dis > 0):
            crowded_breed.append(int(breed))

    if len(crowded_breed) == 0:
        return -1
    else:
        return max(crowded_breed)
