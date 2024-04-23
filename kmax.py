import random

random.seed(616)


def partition(array, left, right):
    start_idx = left
    pivot = array[right]
    for i in range(left, right):
        if array[i] <= pivot:
            array[start_idx], array[i] = array[i], array[start_idx]
            start_idx = start_idx + 1

    array[start_idx], array[right] = array[right], array[start_idx]
    return start_idx


def main(array, low, high, k):
    if low < high:
        idx = partition(array, low, high)
        print(idx)
        if k >= idx + 1:
            main(array, low, idx - 1, k)
        else:
            main(array, idx + 1, high, k)


if __name__ == "__main__":
    array = [i for i in range(-100, 100)]
    array = random.sample(array, 10)
    main(array, 0, len(array) - 1, 3)
    print(array)
