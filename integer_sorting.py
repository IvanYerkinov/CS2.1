
def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    maxdigit = 0
    mindigit = 0
    outputlist = []
    # TODO: Create list of counts with a slot for each number in input range
    le = {}
        # TODO: Loop over given numbers and increment each number's count
    for i in numbers:
        if i > maxdigit:
            maxdigit = i
        if i < mindigit:
            mindigit = i
        if i in le:
            le[i] += 1
        else:
            le[i] = 1
        # TODO: Loop over counts and append that many numbers into output list
        for i in range(mindigit, maxdigit+1):
            if i in le:
                for y in range(0, le[i]):
                    outputlist.append(i)
        return outputlist


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    arr = []

    for i in range(num_buckets):
        arr.append([])

    for i in numbers:
        ind = int(num_buckets * i)
        arr[ind].append(i)

    for i in range(num_buckets):
        arr[i] = counting_sort(arr[i])

    i = 0
    ret = []
    for y in range(num_buckets):
        for j in range(len(arr[y])):
            ret[i] = arr[i][j]
            i += 1
    return ret
