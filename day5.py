f = open("in.txt", "r")
input = f.read()
lines = input.splitlines()
rules = [tuple(arr) for arr in [el.split("|") for el in lines[: lines.index("")]]]
updates = [el.split(",") for el in lines[lines.index("") + 1 :]]
import networkx as nx


def correct(l):
    return all((a, b) in rules for a, b in zip(l, l[1:]))


def part1(s):
    count = 0
    corrects = []
    for i in range(len(updates)):
        if correct(updates[i]):
            corrects.append(i)
            count += 1
    return sum(int(updates[c][int(len(updates[c]) / 2)]) for c in corrects)


def part2(s):
    count = 0
    corrects = []
    incorect = []
    for i in range(len(updates)):
        if correct(updates[i]):
            corrects.append(i)
            count += 1
        else:
            incorect.append(i)
    corrected = []

    for i in incorect:
        G = nx.DiGraph()
        G.clear()
        G.add_nodes_from(updates[i])
        for before, after in rules:
            if before in updates[i] and after in updates[i]:
                G.add_edge(before, after)
        good = list(nx.topological_sort(G))
        corrected.append(good)

    return sum(int(c[int(len(c) / 2)]) for c in corrected)


print(part1(input))
print(part2(input))
