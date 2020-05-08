def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Implement Cache
    cache = {}

    def helper(arr, index=0):
        # default index to 0
        if index == len(weights):
            return
        # ends if at end of index

        for i in range(index+1, len(weights)):
            # increment index for each I until end of weights list
            # set range to next index to end

            sum = weights[index] + weights[i]
            # set sum to current i plus index

            if sum not in cache:
                if i > index:
                    cache[sum] = (i, index)
                else:
                    cache[sum] = (index, i)
            # if the sum is not already in index, sets higher index to[0] and lower to [1] of sum

            helper(weights, index+1)

    # recurse until limit is reached
    helper(weights)
    if limit in cache:
        return cache[limit]
    else:
        return None

# Given a package with a weight limit 'limit' and a list 'weights' of item weights, implement a function
# get_indices_of_item_weights that finds two items whose sum of weights equals the weight limit limit.
# Your function will return an instance of an Answer tuple that has the following form:
#
# (zero, one) where each element represents the item weights of the two packages.
# The higher valued index should be placed in the zeroth index and the smaller index should be placed in the first index.
# If such a pair doesn’t exist for the given inputs, your function should return None.
#
# Your solution should run in linear time.
#
# Example:
#
# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

# A brute-force solution would involve two nested loops, yielding a quadratic-runtime solution.
# How can we use a hash table in order to implement a solution with a better runtime?
#
# Think about what we can store in the hash table in order to help us to solve this problem more efficiently.
#
# What if we store each weight in the input list as keys?
# What would be a useful thing to store as the value for each key?
#
# If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for
# limit - weight. If it does, then we've found the two items whose weights sum up to the limit!