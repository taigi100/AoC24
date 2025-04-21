# f = open("in.txt", "r")
f = open("ex.txt", "r")
import re

lines = f.read().splitlines()
robots = [
    (
        [int(r) for r in re.findall(r"-*\d+", line.split()[0])][::-1],
        [int(r) for r in re.findall(r"-*\d+", line.split()[1])][::-1],
    )
    for line in lines
]
n, m = 103, 101
seconds = 100


# def print_rob():
#     pos = [r[0] for r in robots]
#     print(pos)
#     for i in range(n):
#         for j in range(m):
#             c = pos.count([i, j])
#             v = c if c != 0 else "."
#             print v,
#         print ("---", i)


def solve():
    for s in range(10000000):
        seen = set()
        for k, r in enumerate(robots):
            px, py = r[0]
            vx, vy = r[1]
            nx, ny = [(px + vx * s) % n, (py + vy * s) % m]
            seen.add((nx, ny))
        print(len(seen), len(robots))
        if len(seen) == len(robots):
            return s

    # pos = [r[0] for r in robots]
    # mid_x = n // 2
    # mid_y = m // 2
    # quadrants = [0] * 4
    # for x, y in pos:
    #     if x < mid_x and y < mid_y:
    #         quadrants[0] += 1
    #     if x > mid_x and y < mid_y:
    #         quadrants[1] += 1
    #     if x < mid_x and y > mid_y:
    #         quadrants[2] += 1
    #     if x > mid_x and y > mid_y:
    #         quadrants[3] += 1
    # ans = 1
    # for q in quadrants:
    #     ans *= q


print(solve())
