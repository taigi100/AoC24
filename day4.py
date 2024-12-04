f = open("in.txt", "r")
input = f.read()


def part1(s: str):
    grid = s.splitlines()
    N = len(grid)
    M = len(grid[0])
    letters = ["M", "A", "S"]
    dir_x = [0, 0, 1, 1, 1, -1, -1, -1]
    dir_y = [1, -1, -1, 0, 1, -1, 0, 1]
    words = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "X":
                for z in range(len(dir_x)):
                    found = 1
                    for k in range(len(letters)):
                        dist = k + 1
                        x = i + dist * dir_x[z]
                        y = j + dist * dir_y[z]
                        if x >= N or x < 0 or y >= M or y < 0:
                            found = 0
                            continue
                        if grid[x][y] != letters[k]:
                            found = 0
                    words = words + found
    return words


def part2(s: str):
    grid = s.splitlines()
    N = len(grid)
    M = len(grid[0])
    lines = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
    words = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "A":
                found = 0
                for k in range(len(lines)):
                    x1 = i + lines[k][0][0]
                    y1 = j + lines[k][0][1]
                    x2 = i + lines[k][1][0]
                    y2 = j + lines[k][1][1]
                    if (
                        x1 >= N
                        or x2 >= N
                        or x1 < 0
                        or x2 < 0
                        or y1 >= M
                        or y2 >= M
                        or y1 < 0
                        or y2 < 0
                    ):
                        found = 0
                        continue
                    if (grid[x1][y1] == "M" and grid[x2][y2] == "S") or (
                        grid[x1][y1] == "S" and grid[x2][y2] == "M"
                    ):
                        found += 1
                if found == 2:
                    words = words + 1
    return words


print(part1(input))
print(part2(input))
