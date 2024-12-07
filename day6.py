f = open("in.txt", "r")
# f = open("ex.txt", "r")
input = f.read()
lines = input.splitlines()
N = len(lines)
M = len(lines[0])
start = ()
for i, l in enumerate(lines):
    if "^" in l:
        t = l.index("^")
        start = (i, t)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()


def in_range(dx, dy):
    return not (dx < 0 or dy < 0 or dx >= N or dy >= M)


def part1(location, dir):
    dx, dy = (location[0] + dir[0], location[1] + dir[1])
    while True:
        while in_range(dx, dy) and lines[dx][dy] == "#":
            dir = dirs[(dirs.index(dir) + 1) % len(dirs)]
            dx, dy = (location[0] + dir[0], location[1] + dir[1])
        while in_range(dx, dy) and (lines[dx][dy] == "." or lines[dx][dy] == "^"):
            location = (dx, dy)
            visited.add(location)
            dx, dy = (location[0] + dir[0], location[1] + dir[1])
        if not in_range(dx, dy):
            break
    return len(visited)


def part2(s):
    c = 0

    for i in range(N):
        for j in range(M):
            if lines[i][j] != ".":
                continue

            l, d = s, dirs[0]
            v = set()
            while in_range(l[0], l[1]) and (l, d) not in v:
                v.add((l, d))
                dx, dy = (l[0] + d[0], l[1] + d[1])
                if in_range(dx, dy) and (lines[dx][dy] == "#" or (dx, dy) == (i, j)):
                    d = dirs[(dirs.index(d) + 1) % len(dirs)]
                else:
                    l = (dx, dy)
            c += (l, d) in v
    return c


print(part1(start, dirs[0]))
print(part2(start))
