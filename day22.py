from itertools import product

import numpy as np

# f = open("in.txt", "r")
f = open("ex.txt", "r")

nums = [int(num) for num in f.read().splitlines()]
# nums = [123]
# it = 10
it = 2000


def calc_next(x):
    ans = (x ^ (x << 6)) & 16777215  # 6 bits remain the same
    ans = (ans ^ (ans >> 5)) & 16777215
    ans = (ans ^ (ans << 11)) & 16777215
    return ans


def search(text, pattern):
    for i in range(len(text)):
        if text[i : i + len(pattern)] == pattern:
            return i + len(pattern)


def part1():
    cache = {}
    results = []
    series = []
    for k, num in enumerate(nums):
        series.append([num % 10])
        for i in range(it):
            next = 0
            if num in cache:
                next = cache[num]
            else:
                next = calc_next(num)
                cache[num] = next
            num = next
            series[k].append(num % 10)
        results.append(num)
    print(sum(results))

    diffs = [[b - a for a, b in zip(s, s[1:])] for s in series]
    flat_diffs = [d for sublist in diffs for d in sublist]
    windows = np.lib.stride_tricks.sliding_window_view(flat_diffs, 4)
    print("1")
    unique = np.unique(windows, axis=0)
    print("2")
    print(len(unique))

    print("before")
    window_to_price = []
    for k, d in enumerate(diffs):
        window_to_price.append({})
        for i in range(len(d) - 4):
            key = tuple(d[i : i + 4])
            price = series[k][i + 4]
            if key not in window_to_price[k]:
                window_to_price[k][key] = price

    print("after")
    p2 = 0
    print(len(windows))
    for k, p in enumerate(unique):
        s = 0
        for k, d in enumerate(diffs):
            key = tuple(p)
            if key in window_to_price[k]:
                s += window_to_price[k][key]
        if s > p2:
            print(p, s)
            p2 = s
    print(p2)


def part2():
    pass


part1()
