f = open("in.txt", "r")
# f = open("ex.txt", "r")
import re

grid, moves = f.read().split("\n\n")
grid = [list(line) for line in grid.splitlines()]
moves = "".join(moves.splitlines())
print(moves)
N, M = len(grid), len(grid[0])

def print_grid(q):
    print('----')
    for i in range(len(q)):
        for j in range(len(q[0])):
            print q[i][j],
        print
    print('----')

start = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == "@"][0]

dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def in_bounds(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


def part1():

    x, y = start
    for move in moves:
        nx, ny = (x + dirs[move][0], y + dirs[move][1])
        if not in_bounds(nx, ny, N, M):
            continue
        if grid[nx][ny] == "#":
            continue
        if grid[nx][ny] == ".":
            grid[x][y] = "."
            grid[nx][ny] = "@"
            x, y = nx, ny
        if grid[nx][ny] == "O":
            # Go in the direction, if you find 'O' switch, if you find '#' continue
            nnx, nny = nx, ny
            found = "O"
            while in_bounds(nnx, nny, N, M) and found == "O":
                nnx, nny = (nnx + dirs[move][0], nny + dirs[move][1])
                if in_bounds(nnx, nny, N, M) and grid[nnx][nny] == "#":
                    found = "#"
                if in_bounds(nnx, nny, N, M) and grid[nnx][nny] == ".":
                    found = "."
            if found == ".":
                grid[nnx][nny] = "O"
                grid[nx][ny] = "@"
                grid[x][y] = "."
                x,y = nx, ny

    return sum(100 * i + j for i in range(N) for j in range(M) if grid[i][j] == "O")

def part2():
    #expand
    g = []
    for l in grid:
        g.append([])
        for c in l:
            if c == '#':
                g[len(g)-1].append("#")
                g[len(g)-1].append("#")
            elif c == "O":
                g[len(g)-1].append("[")
                g[len(g)-1].append("]")
            elif c == ".":
                g[len(g)-1].append(".")
                g[len(g)-1].append(".")
            elif c == "@":
                g[len(g)-1].append("@")
                g[len(g)-1].append(".")
    
    N, M = len(g), len(g[0])
    start = [(i, j) for i in range(N) for j in range(M) if g[i][j] == "@"][0]
    #redo, a bit modified
    x, y = start
    print(moves)
    for move in moves:
        nx, ny = (x + dirs[move][0], y + dirs[move][1])
        if not in_bounds(nx, ny, N, M):
            continue
        if g[nx][ny] == "#":
            continue
        if g[nx][ny] == ".":
            g[x][y] = "."
            g[nx][ny] = "@"
            x, y = nx, ny
        if g[nx][ny] == "[" or g[nx][ny] == "]":
            # Go in the direction, if you find 'O' switch, if you find '#' continue
            nnx, nny = nx, ny
            found = "O"
            print("Found box")
            while in_bounds(nnx, nny, N, M) and found == "O":
                nnx, nny = (nnx + dirs[move][0], nny + dirs[move][1])
                if in_bounds(nnx, nny, N, M) and g[nnx][nny] == "#":
                    found = "#"
                if in_bounds(nnx, nny, N, M) and g[nnx][nny] == ".":
                    found = "."
            if found == ".":
                print("found empty")
                #Fill up properly from nx,ny + dir to nnx, nny
                nfill = g[nx][ny]
                tx, ty = nx, ny
                tx, ty = (tx + dirs[move][0], ty + dirs[move][1])
                while (tx, ty) != (nnx, nny):
                     g[tx][ty] = nfill
                     nfill = ']' if nfill is '[' else '['
                     tx, ty = (tx + dirs[move][0], ty + dirs[move][1])
                g[tx][ty] = nfill
                g[nx][ny] = "@"
                g[x][y] = "."
                x,y = nx, ny
        print("Move ", move)
        print_grid(g)
                
    return sum(100 * i + j for i in range(N) for j in range(M) if g[i][j] == "[")



# print(part1())
print(part2())
