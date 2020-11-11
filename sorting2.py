def mergeSort(lis):
    if len(lis) > 1:
        mid = len(lis)//2
        left = lis[:mid]
        right = lis[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lis[k] = left[i]
                i += 1
            else:
                lis[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lis[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lis[k] = right[j]
            j += 1
            k += 1


def part(lis, low, high):
    i = low-1
    p = lis[high]

    for j in range(low, high):
        if lis[j] < p:
            i += 1
            lis[i], lis[j] = lis[j], lis[i]

    lis[i+1], lis[high] = lis[high], lis[i+1]
    return i + 1


def quickSort(lis, low, high):
    if low < high:
        p = part(lis, low, high)

        quickSort(lis, low, p-1)
        quickSort(lis, p+1, high)


test1 = [5, 8, 2, 4, 1]
test2 = [9, 2, 4, 1, 2]

mergeSort(test1)
quickSort(test2, 0, len(test2)-1)

print(test1)
print(test2)
