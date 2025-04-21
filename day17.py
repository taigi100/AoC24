# f = open("in.txt", "r")
f = open("ex.txt", "r")
import re

data = f.read().split("\n\n")
A, B, C = [int(nr) for nr in re.findall(r"\d*", data[0]) if nr]
ops = [int(nr) for nr in re.findall(r"\d*", data[1]) if nr]

ip = 0


def solve(ip):
    global A, B, C
    sol = []

    def get_op_value(op):
        if op == 4:
            return A
        elif op == 5:
            return B
        elif op == 6:
            return C
        return op

    while ip + 1 < len(ops):

        ins = ops[ip]
        op = ops[ip + 1]

        # print()
        # print(ip)
        # print(A, B, C)
        # print(ins, get_op_value(op))
        # print()
        #
        if op == 7:
            ip += 2

        match ins:
            case 0:
                A = A // pow(2, get_op_value(op))
                ip += 2
            case 1:
                B = B ^ op
                ip += 2
            case 2:
                B = get_op_value(op) % 8
                ip += 2
            case 3:
                if A != 0:
                    ip = op
                else:
                    ip += 2
            case 4:
                B = B ^ C
                ip += 2
            case 5:
                # print(get_op_value(op) % 8, end=",")
                sol.append(get_op_value(op) % 8)
                ip += 2
            case 6:
                B = A // pow(2, get_op_value(op))
                ip += 2
            case 7:
                C = A // pow(2, get_op_value(op))
                ip += 2
    return sol


solve(0)


def solve_one(x):
    return (((x & 7) ^ 6) ^ (x >> (x & 7 ^ 3))) & 7


quines = []

for num in reversed(ops):
    new_quines = [0]
    for curr in quines:
        for i in range(8):
            val = (curr << 3) + i
            if solve_one(val) == num:
                new_quines.append(val)
    quines = new_quines
    print(quines)
