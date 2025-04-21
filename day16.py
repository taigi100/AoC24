# f = open("in.txt", "r")
f = open("ex.txt", "r")
import re

grid = [list(line) for line in f.read().splitlines()]
N, M = len(grid), len(grid[0])
nodes = set()

start = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == "S"][0]
end = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == "E"][0]

dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
scores = {}  # dict of position, facing = distance


def in_bounds(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


def get_rotated_dirs(dir):
    return [(-1, 0), (1, 0)] if dir[0] == 0 else [(0, -1), (0, 1)]


def solve():
    keys = [(start, d) for d in dirs]
    scores[(start, dirs[0])] = 0
    scores[(start, dirs[1])] = 1000
    scores[(start, dirs[2])] = 1000
    scores[(start, dirs[3])] = 2000

    q = set(keys)
    while q:
        s, d = q.pop()
        nx, ny = (s[0] + d[0], s[1] + d[1])
        if grid[nx][ny] == "#":
            continue

        for di in [d, *get_rotated_dirs(d)]:
            new_val = scores[(s, d)] + (1001 if d != di else 1)
            ns = ((nx, ny), di)
            if new_val < scores.get(ns, float("inf")):
                scores[ns] = new_val
                q.add(ns)

    p1 = min(scores[end, d] for d in dirs)

    paths = []
    seen = set()

    def back(c, path):
        if path and c[0] == start:
            paths.append(path[:])
            return

        if c in seen:
            return
        seen.add(c)

        prev_loc = []
        for d in [c[1], *get_rotated_dirs(c[1])]:
            mirrored = (d[0] * -1, d[1] * -1)
            px, py = (c[0][0] + mirrored[0], c[0][1] + mirrored[1])
            p = (px, py)
            if grid[px][py] == "#":
                continue
            prev_loc.append((p, d))

            scoredif = 1001 if d != c[1] else 1
            if (
                scores.get((c[0], c[1]), float("inf"))
                - scores.get((p, d), float("inf"))
                == scoredif
            ):
                back((p, d), [(p, d)] + path)

        seen.remove(c)

    for d in dirs:
        if scores.get((end, d), float("inf")) == p1:
            back((end, d), [(end, d)])

    for path in paths:
        for node in path:
            nodes.add(node[0])
    p2 = len(nodes)
    return (p1, p2)


print(solve())
