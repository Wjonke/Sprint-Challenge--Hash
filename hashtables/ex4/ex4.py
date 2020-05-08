def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}

    result = []
    for i in a:
        if -i in cache:
            # if there is a negative version of the index

            result.append(i if i >= 0 else -i)
            # makes it so what is appended is a positive # regardless

        cache[i] = 1
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))

# For an input list of integers, we wish to know which positive numbers have corresponding negative numbers in the list.
#
# Example input:
#
# [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
# Input can be in any order.
#
# Example return value:
#
# [ 1, 3, 4 ]
# Because 1, 3, and 4 are the positive numbers that have corresponding negative numbers in the list.
#
# Return value can be in any order.
#
# Solve this problem with a hash table.
#
# Limits:
#
# The input list can contain approximately 5,000,000 elements.
