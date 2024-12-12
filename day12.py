# f = open("in.txt", "r")
f = open("ex.txt", "r")

grid = f.read().strip("\n").splitlines()
N, M = len(grid), len(grid[0])
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < M


def solve():
    seen = set()
    p1, p2 = 0, 0

    def fill(i, j):
        a = 0
        p = 0
        q = {(i, j)}
        borders = {(dx, dy): [] for dx, dy in d}
        while q:
            x, y = q.pop()
            seen.add((x, y))
            a += 1
            for dx, dy in d:
                nx, ny = (x + dx, y + dy)
                if not in_bounds(nx, ny):
                    p += 1
                    borders[(dx, dy)].append((nx, ny))
                    continue
                else:
                    if grid[x][y] != grid[nx][ny]:
                        p += 1
                        borders[(dx, dy)].append((nx, ny))
                        continue
                    elif (nx, ny) not in seen:
                        q.add((nx, ny))
        sides = count_sides(borders)
        return (a, p, sides)

    def count_sides(borders):
        sides = 0
        for dx, dy in d:
            m = 0 if (dx, dy) in [(1, 0), (-1, 0)] else 1
            o = 1 - m
            borders[(dx, dy)].sort(key=lambda x: (x[m], x[o]))

            pm, po = -2, -2
            for b in borders[(dx, dy)]:
                if pm == -2 or pm != b[m] or b[o] - po > 1:
                    sides += 1
                pm, po = b[m], b[o]
        return sides

    for i in range(N):
        for j in range(M):
            if (i, j) not in seen:
                area, permiter, sides = fill(i, j)
                print(grid[i][j], " ", area, "x", permiter, "x", sides)
                p1 += area * permiter
                p2 += area * sides
    return p1, p2


print(solve())
