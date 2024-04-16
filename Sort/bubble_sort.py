import random
random.seed(616)


def sort_easy(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


input = random.sample([i for i in range(100)], 10)
output = sort_easy(input)
print(output)