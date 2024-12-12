# f = open("in.txt", "r")
f = open("ex.txt", "r")

stones = f.read().strip("\n").split()
stones = [int(el) for el in stones]
print(stones)


def part1():
    blinks = 5
    for b in range(blinks):
        for k in range(len(stones) - 1, -1, -1):
            v = stones[k]
            if v == 0:
                stones[k] = 1
            elif len(str(v)) % 2 == 0:
                stones[k] = int(str(v)[: len(str(v)) // 2])
                stones.insert(k + 1, int(str(v)[len(str(v)) // 2 :]))
            else:
                stones[k] *= 2024
    return len(stones)


def part2():
    blinks = 75
    cache = {}

    def blink(stone, n):
        key = (stone, n)
        if key in cache:
            return cache[key]
        if n == 0:
            cache[key] = 1
            return 1
        if stone == 0:
            ans = blink(1, n - 1)
            cache[key] = ans
            return ans
        if len(str(stone)) % 2 == 0:
            l = int(str(stone)[: len(str(stone)) // 2])
            r = int(str(stone)[len(str(stone)) // 2 :])
            ans = blink(l, n - 1) + blink(r, n - 1)
            cache[key] = ans
            return ans
        ans = blink(2024 * stone, n - 1)
        cache[key] = ans
        return ans

    r = 0
    for i in stones:
        r += blink(i, blinks)
    return r


# print(part1())
print(part2())
