# f = open("in.txt", "r")
f = open("ex.txt", "r")

map = f.read().strip("\n").splitlines()
map = [[int(el) for el in line] for line in map]
N, M = len(map), len(map[0])
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < M


def part1():
    starts = [(x, y) for x in range(N) for y in range(M) if map[x][y] == 0]
    ans = 0
    for s in starts:
        q, viz = {s}, set()
        score = 0

        while q:
            x, y = q.pop()
            viz.add((x, y))
            if map[x][y] == 9:
                score += 1
                continue

            q.update(
                (x + dx, y + dy)
                for dx, dy in d
                if in_bounds(x + dx, y + dy)
                and map[x + dx][y + dy] == map[x][y] + 1
                and (x + dx, y + dy) not in viz
            )
        ans += score
    return ans


def part2():
    starts = [(x, y) for x in range(N) for y in range(M) if map[x][y] == 0]
    ans = 0
    for s in starts:
        q, rating = {s}, [[0 for _ in line] for line in map]
        while q:
            x, y = q.pop()
            rating[x][y] += 1

            q.update(
                (x + dx, y + dy)
                for dx, dy in d
                if in_bounds(x + dx, y + dy) and map[x + dx][y + dy] == map[x][y] + 1
            )
        ans += sum(rating[x][y] for x in range(N) for y in range(M) if map[x][y] == 9)
    return ans


print(part1())
print(part2())
