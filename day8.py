# f = open("in.txt", "r")
import itertools

f = open("ex.txt", "r")
input = f.read()
lines = input.splitlines()
N = len(lines)
M = len(lines[0])
antenas = {}
ant = []
antenas_cnt = 0
for i in range(N):
    for j in range(M):
        if lines[i][j] != ".":
            antenas_cnt += 1
            if lines[i][j] in antenas:
                antenas[lines[i][j]].append((i, j))
                ant.append((i, j))
            else:
                antenas[lines[i][j]] = [(i, j)]
                ant.append((i, j))


def part1():
    antinodes = set()
    for k, v in antenas.items():
        for pair in itertools.combinations(antenas[k], 2):
            l, r = pair[0], pair[1]
            x1 = (2 * l[0] - r[0], 2 * l[1] - r[1])
            x2 = (2 * r[0] - l[0], 2 * r[1] - l[1])
            if x1[0] >= 0 and x1[0] < N and x1[1] >= 0 and x1[1] < M:
                antinodes.add(x1)
            if x2[0] >= 0 and x2[0] < N and x2[1] >= 0 and x2[1] < M:
                antinodes.add(x2)
    return len(antinodes)


def part2():
    antinodes = set()
    for k, v in antenas.items():
        for pair in itertools.combinations(antenas[k], 2):
            l, r = pair[0], pair[1]
            added = True
            multiplier = 1
            while added:
                added = False
                x1 = (
                    multiplier * (l[0] - r[0]) + l[0],
                    multiplier * (l[1] - r[1]) + l[1],
                )
                x2 = (
                    multiplier * (r[0] - l[0]) + r[0],
                    multiplier * (r[1] - l[1]) + r[1],
                )
                if x1[0] >= 0 and x1[0] < N and x1[1] >= 0 and x1[1] < M:
                    antinodes.add(x1)
                    added = True
                if x2[0] >= 0 and x2[0] < N and x2[1] >= 0 and x2[1] < M:
                    antinodes.add(x2)
                    added = True
                multiplier += 1
    # for i in range(N):
    #     for j in range(M):
    #         if (i, j) in antinodes:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
    for p in ant:
        antinodes.add(p)
    return len(antinodes)


print(part1())
print(part2())
