from collections import defaultdict

# f = open("in.txt", "r")
f = open("ex.txt", "r")

initValues, operations = f.read().split("\n\n")
initValues = initValues.splitlines()
operations = operations.splitlines()

value = {}
ops = defaultdict(list)

for line in initValues:
    k, v = line.split(": ")
    v = int(v)
    value[k] = v

for line in operations:
    x1, op, x2, _, res = line.split(" ")
    ops[(x1, op, x2)].append(res)

print(ops)
while ops:
    toDelete = []
    for x1, op, x2 in ops:
        res = ops[(x1, op, x2)]
        if x1 in value and x2 in value:
            ans = 0
            if op == "AND":
                ans = value[x1] & value[x2]
            elif op == "XOR":
                ans = value[x1] ^ value[x2]
            elif op == "OR":
                ans = value[x1] | value[x2]
            for v in res:
                value[v] = ans
            toDelete.append((x1, op, x2))
    for k in toDelete:
        del ops[k]

z_map = [(k, value[k]) for k in value if k[0] == "z"]
z_map.sort(key=lambda p: p[0])
ans = 0
for i in range(len(z_map)):
    ans += (1 << i) * z_map[i][1]
for k in z_map:
    print(k[1], end=",")
print(ans)
