# f = open("in.txt", "r")
f = open("ex.txt", "r")
from heapq import heappop, heappush

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
grid = [list(line) for line in f.read().splitlines()]
N, M = len(grid), len(grid[0])

start = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == "S"][0]
end = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == "E"][0]


def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < N


def part1():
    pass


def part2():
    pass


print(part2())
