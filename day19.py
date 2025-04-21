# f = open("in.txt", "r")
f = open("ex.txt", "r")

data = f.read()
towels = data.split("\n\n")[0].split(", ")
designs = data.split("\n\n")[1].splitlines()


def solve():
    p1, p2 = 0, 0
    for design in designs:
        dp = [1 if design[0] in towels else 0]
        for i in range(1, len(design)):
            dp.append(
                (1 if design[: i + 1] in towels else 0)
                + sum(
                    dp[j]
                    for j in range(i - 1, -1, -1)
                    if design[j + 1 : i + 1] in towels
                )
            )

        p1 += 1 if dp[len(design) - 1] > 0 else 0
        p2 += dp[len(design) - 1]
    print(p1, p2)


solve()
