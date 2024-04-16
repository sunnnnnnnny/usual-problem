import random
random.seed(616)


def sort_easy(array):
    max_val = max(array)
    min_val = min(array)
    bucket_list = [[] for _ in range(max_val - min_val + 1)]
    for val in array:
        diff = val - min_val
        bucket_list[diff].append(0)
    res_array = []
    for diff in range(len(bucket_list)):
        if len(bucket_list[diff]) > 0:
            res_array = res_array + [min_val + diff for _ in range(len(bucket_list[diff]))]
    return res_array


input = random.sample([i for i in range(-100, 100)], 10)
print(input)
output = sort_easy(input)
input.sort()
print(input)
print(output)