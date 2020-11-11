def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
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
    # Stretch: Improve this to mutate input instead of creating new output list


#TODO: Write some test cases
testcase = [4, 2, 101, 1, 3, 3, -2, 100]

print(counting_sort(testcase))
