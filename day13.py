# f = open("in.txt", "r")
f = open("ex.txt", "r")
import re

games = f.read().split("\n\n")


def solve_linear_system(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p

    n1 = (px * by - py * bx) / (ax * by - ay * bx)
    n2 = (py * ax - px * ay) / (ax * by - ay * bx)

    return n1, n2


def part1():
    p1 = 0
    for game in games:
        a = [int(el) for el in re.findall(r"[0-9]+", game.splitlines()[0])]
        b = [int(el) for el in re.findall(r"[0-9]+", game.splitlines()[1])]
        g = [int(el) for el in re.findall(r"[0-9]+", game.splitlines()[2])]
        # need n, m so that n * a + m * b = g where m as big as possible
        n1, n2 = solve_linear_system(a, b, g)
        if n1 % 1 == 0 and n2 % 1 == 0 and n1 <= 100 and n2 <= 100:
            p1 += 3 * int(n1) + int(n2)
            print(a, b, g, n1, n2, int(n2) + 3 * int(n1))

    return p1


def part2():
    p2 = 0
    for game in games:
        a = [int(el) for el in re.findall(r"[0-9]+", game.splitlines()[0])]
        b = [int(el) for el in re.findall(r"[0-9]+", game.splitlines()[1])]
        g = [
            int(el) + 10000000000000
            for el in re.findall(r"[0-9]+", game.splitlines()[2])
        ]
        # need n, m so that n * a + m * b = g where m as big as possible
        n1, n2 = solve_linear_system(a, b, g)
        if (
            n1 % 1 == 0
            and n2 % 1 == 0
            and n1 >= 100
            and n2 >= 100
            and a[0] * n1 + b[0] * n2 == g[0]
            and a[1] * n1 + b[1] * n2 == g[1]
        ):
            p2 += 3 * int(n1) + int(n2)
            print(a, b, g, n1, n2, int(n2) + 3 * int(n1))

    return p2


print(part1())
print(part2())
