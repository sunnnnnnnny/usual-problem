import random
random.seed(616)


def merge(array, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid + 1 - 1
    list_l = [0] * n1
    list_r = [0] * n2
    for i in range(0, n1):
        list_l[i] = array[low + i]
    for j in range(0, n2):
        list_r[j] = array[mid + 1 + j]
    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        if list_l[i] <= list_r[j]:
            array[k] = list_l[i]
            i = i + 1
        else:
            array[k] = list_r[j]
            j = j + 1
        k = k + 1
    while i < n1:
        array[k] = list_l[i]
        k = k + 1
        i = i + 1
    while j < n2:
        array[k] = list_r[j]
        k = k + 1
        j = j + 1


def sort_middle(array, low, high):
    if low < high:
        m = (low + high - 1) // 2
        sort_middle(array, low, m)
        sort_middle(array, m+1, high)
        merge(array, low, m, high)


input = random.sample([i for i in range(-100, 100)], 10)
sort_middle(input, 0, len(input)-1)
print(input)
