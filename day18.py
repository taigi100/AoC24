# f = open("in.txt", "r")
f = open("ex.txt", "r")
import re
from heapq import heappop, heappush

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bytes = [tuple(map(int, re.findall(r"\d+", line))) for line in f.read().splitlines()]
bytes = [tuple(reversed(pair)) for pair in bytes]
N = 71


def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < N


def part1():
    b = bytes[:1024]
    q = [(0, (0, 0))]
    seen = set()
    cost = {(0, 0): 0}

    while q:
        c, (x, y) = heappop(q)
        if (x, y) in seen:
            continue
        seen.add((x, y))

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not in_bounds(nx, ny) or (nx, ny) in b:
                continue
            nc = cost[x, y] + 1
            if nc < cost.get((nx, ny), float("inf")):
                cost[nx, ny] = nc
                heappush(q, (nc, (nx, ny)))

    return cost[(N - 1, N - 1)]


def part2():
    for i in range(1024, len(bytes)):
        print(i)
        b = bytes[:i]
        q = [(0, (0, 0))]
        seen = set()
        cost = {(0, 0): 0}

        while q:
            c, (x, y) = heappop(q)
            if (x, y) in seen:
                continue
            seen.add((x, y))

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not in_bounds(nx, ny) or (nx, ny) in b:
                    continue
                nc = c + 1
                if nc < cost.get((nx, ny), float("inf")):
                    cost[nx, ny] = nc
                    heappush(q, (nc, (nx, ny)))
        if (N - 1, N - 1) not in cost:
            return b[len(b) - 1]


print(part2())
