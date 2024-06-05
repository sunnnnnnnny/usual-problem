def get_result(array):
    res = min(array)
    cur_sum = 0
    for idx in range(len(array)):
        cur_sum = max(cur_sum + array[idx], array[idx])
        res = max(cur_sum, res)
    return res


if __name__ == "__main__":
    array = [1, 4, -5, 9, 8, 3, -6]
    out = get_result(array)
    print(out)
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    out = get_result(array)
    print(out)
