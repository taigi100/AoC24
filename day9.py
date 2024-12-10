# f = open("in.txt", "r")
f = open("ex.txt", "r")

map = f.read().strip("\n")

arr = []
alt = 1
for k, v in enumerate(map):
    arr.append([k // 2] * int(v) if alt == 1 else [-1] * int(v))
    alt = 1 - alt
unzipped = arr
arr = [item for sub in arr for item in sub]


def part1():
    left, right = 0, len(arr) - 1

    while left < right:
        while right >= 0 and arr[right] == -1:
            right -= 1
        while left <= len(arr) and arr[left] != -1:
            left += 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    return sum([k * v for k, v in enumerate(arr) if v != -1])


def part2():
    end = len(unzipped) - 1

    while end >= 0:
        while end >= 0 and (len(unzipped[end]) == 0 or unzipped[end][0] == -1):
            end -= 1
        idx = 0
        while idx < end and (
            len(unzipped[idx]) == 0
            or len(unzipped[idx]) < len(unzipped[end])
            or unzipped[idx][0] != -1
        ):
            idx += 1

        if len(unzipped[idx]) > 0 and idx < end and unzipped[idx][0] == -1:
            remaining = [-1] * (len(unzipped[idx]) - len(unzipped[end]))
            unzipped[idx] = unzipped[end]
            unzipped[end] = [-1] * len(unzipped[idx])
            unzipped.insert(idx + 1, remaining)
        end -= 1

    fin = [item for sub in unzipped for item in sub]
    return sum([k * v for k, v in enumerate(fin) if v != -1])


print(part1())
print(part2())
