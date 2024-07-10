def get_result(array):
    res = min(array)
    past_sum = 0
    for idx in range(len(array)):
        past_sum = max(past_sum + array[idx], array[idx])
        res = max(past_sum, res)
    return res


if __name__ == "__main__":
    array = [1, 4, -5, 9, 8, 3, -6]
    out = get_result(array)
    print(out)
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    out = get_result(array)
    print(out)
