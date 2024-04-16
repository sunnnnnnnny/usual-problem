import random
random.seed(616)


def partition(array, low, high):
    left = low
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            array[j], array[left] = array[left], array[j]
            left = left + 1
    array[left], array[high] = array[high], array[left]
    return left


def sort_middle(array, low, high):
    if low < high:
        part_idx = partition(array, low, high)
        sort_middle(array, low, part_idx-1)
        sort_middle(array, part_idx + 1, high)


input = random.sample([i for i in range(-100, 100)], 10)
sort_middle(input, 0, len(input)-1)
print(input)
