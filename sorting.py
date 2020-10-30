#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            return False

    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    swap = 1
    while swap == 1:
        swap = 0
        for i in range(len(items) - 1):
            if items[i] > items[i+1]:
                temp = items[i+1]
                items[i+1] = items[i]
                items[i] = temp
                swap = 1

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    end = len(items)
    start = 0
    index = 0

    pas = 1
    while(pas):
        mi = items[start]
        index = start

        for i in range(start, end):
            if mi > items[i]:
                mi = items[i]
                index = i

        items.pop(index)
        items.insert(start, mi)

        start += 1

        if start == end:
            pas = 0


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    for i in range(1, len(items)):

        temp = items[i]

        index = i-1
        while index >= 0 and temp < items[index]:
            items[index+1] = items[index]
            index -= 1
        items[index+1] = temp
