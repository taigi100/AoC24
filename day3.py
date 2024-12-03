f = open("in.txt", "r")
input = f.read()
import re


def part1(s: str):
    matches = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", s)
    num_pattern = r"\d{1,3}"

    return sum(
        int(re.findall(num_pattern, item)[0]) * int(re.findall(num_pattern, item)[1])
        for item in matches
    )


def part2(s: str):
    matches = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)", s)
    sum = 0
    use = True
    num_pattern = r"\d{1,3}"
    for el in matches:
        if el == "do()":
            use = True
        elif el == "don't()":
            use = False
        elif use == True:
            sum += int(re.findall(num_pattern, el)[0]) * int(
                re.findall(num_pattern, el)[1]
            )
    return sum


print(part1(input))
print(part2(input))
