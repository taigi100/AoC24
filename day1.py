f = open("in.txt", "r")
input = f.read()


def part1(s: str):
    left, right = (
        [int(x) for x in col] for col in zip(*[line.split() for line in s.splitlines()])
    )
    left.sort()
    right.sort()
    return sum(abs(a - b) for a, b in zip(left, right))


def part2(s: str):
    left, right = (
        [int(x) for x in col] for col in zip(*[line.split() for line in s.splitlines()])
    )
    freq = {x: right.count(x) for x in right}
    return sum((x * (freq.get(x) or 0)) for x in left)


print(part1(input))
print(part2(input))
