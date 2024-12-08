# f = open("in.txt", "r")
f = open("ex.txt", "r")
import itertools

input = f.read()
lines = input.splitlines()
N, M = len(lines), len(lines[0])
antenas = {}

for i in range(N):
    for j in range(M):
        if lines[i][j] != ".":
            antenas.setdefault(lines[i][j], []).append((i, j))


def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < M


def part1():
    antinodes = set()
    for v in antenas.values():
        for l, r in itertools.combinations(v, 2):
            for p in [
                (2 * l[0] - r[0], 2 * l[1] - r[1]),
                (2 * r[0] - l[0], 2 * r[1] - l[1]),
            ]:
                if in_bounds(*p):
                    antinodes.add(p)
    return len(antinodes)


def part2():
    antinodes = set()
    for v in antenas.values():
        for l, r in itertools.combinations(v, 2):
            multiplier = 1
            while True:
                x1 = (
                    multiplier * (l[0] - r[0]) + l[0],
                    multiplier * (l[1] - r[1]) + l[1],
                )
                x2 = (
                    multiplier * (r[0] - l[0]) + r[0],
                    multiplier * (r[1] - l[1]) + r[1],
                )
                if not any(in_bounds(*p) for p in (x1, x2)):
                    break
                antinodes.update(p for p in (x1, x2) if in_bounds(*p))
                multiplier += 1
    return len(antinodes | set(p for v in antenas.values() for p in v))


print(part1())
print(part2())
