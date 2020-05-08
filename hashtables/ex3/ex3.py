def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    # initialize cache

    result = []
    # initialize result

    for arr in arrays:
        # iterate through arrs in arrays
        for i in arr:
            # iterate through each i in arr
            if i in cache:
                cache[i] += 1
            # if i is in the cache, add +1 to value and move on to next i
            else:
                cache[i] = 1
            # if i is not in cache, add to cache set value to 1

            if cache[i] == len(arrays):
                result.append(i)
            # if cache[i]  = number of arrays passed in, add cache[i] to result
            # (cache[i] exists in all arrays)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # arrays.append([1, 2, 3, 4, 5])
    # arrays.append([2, 3, 4, 5, 6])
    # arrays.append([3, 4, 5, 6, 7])
    # arrays.append([4, 5, 6, 7, 8])
    # arrays.append([4, 5, 6, 7, 8])

    print(intersection(arrays))

# Find the intersection between multiple lists of integers.
#
# Do not use numpy or sets to solve this; use dict or hash-tables, please.
#
# We're given a list of lists that contain integers:
#
# [
#     [1, 2, 3, 4, 5],
#     [12, 7, 2, 9, 1],
#     [99, 2, 7, 1,]
# ]
# And we need to compute the intersection, that is, numbers that exist in all lists.
#
# From the above input, the return value will be:
#
# [1, 2]
# Because those are the numbers that exist in all the lists.
#
# (Output can be in any order.)
#
# Limits:
#
# There can be up to 10 lists in the list of lists.
# The lists can contain up to roughly 1,000,000 elements each.
