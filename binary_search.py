# implementing binary search algorithm

# this is a demonstration proving that binary search
# is faster than "naive" search

import random
import time

# "naive" search: scan each element of a sorted list and ask if it is equal to the target
# Input: a list of elements
# Output: The index of the element in the list that is equal to the target OR
#         if no element equals the target, return -1

def naive_search(l, target):
    # example: l = [1, 3, 10, 12]
    # if 10 is target, should return 2
    for element in range(len(l)):
        if l[element] == target:
            return element
    return -1


def binary_search(l, target, low=None, high=None):
    # divide and conquer algorithm
    # input: a sorted list of element
    # output: The index of the element in the list that is equal to the target OR
    #         if no element equals the target, return -1

    # example l = [1, 3, 5, 10, 12] / target 10 /  alg should return 3
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        # high should never be less than the low
        # if this happens, then the target is not in sorted list
        return -1

    midpoint = (low + high) // 2  # in the example, midpoint = 2

    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l, target, low, high=midpoint-1)
    else:
        # l[midpoint] < target
        return binary_search(l, target, midpoint+1, high)

if __name__=="__main__":
    # TESTING FUNCTIONALITY
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    # to prove binary search is better, building a large list and performing time analysis
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    # searching for every item in the sorted list
    # essentially running the function 10000 times
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    # this is the average time it takes to search using naive search
    print("Naive search time: ", (end-start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
        # this is the average time it takes to search using binary search
    print("Binary search time: ", (end-start)/length, "seconds")
