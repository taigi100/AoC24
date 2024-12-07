# f = open("in.txt", "r")
import itertools

f = open("ex.txt", "r")
input = f.read()
lines = input.splitlines()
N = len(lines)


def part1():
    ans = 0
    for line in lines:
        goal = int(line.split(":")[0])
        nums = [int(num) for num in line.split(":")[1].split()]
        correct = False
        for bits in range(pow(2, len(nums) - 1)):
            val = nums[0]
            for i in range(1, len(nums)):
                if bits & (1 << (i - 1)):
                    val *= nums[i]
                else:
                    val += nums[i]
            if goal == val:
                correct = True
                break
        if correct:
            ans += goal
    return ans


def part2():
    ans = 0
    for line in lines:
        goal = int(line.split(":")[0])
        nums = [int(num) for num in line.split(":")[1].split()]
        correct = False
        for ops in itertools.product(*[("+", "*", "||") for _ in range(len(nums) - 1)]):
            val = nums[0]
            for i in range(1, len(nums)):
                op = ops[i - 1]
                if op == "+":
                    val += nums[i]
                elif op == "*":
                    val *= nums[i]
                elif op == "||":
                    val = int(str(val) + str(nums[i]))
            if goal == val:
                correct = True
                break
        if correct:
            ans += goal
    return ans


print(part1())
print(part2())
