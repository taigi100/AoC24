# f = open("in.txt", "r")
f = open("ex.txt", "r")

import networkx as nx

edges = f.read().splitlines()
G = nx.Graph()

for edge in edges:
    x, y = edge.split("-")
    G.add_node(x)
    G.add_node(y)
    G.add_edge(x, y)


def part1():
    cliques = [clique for clique in nx.enumerate_all_cliques(G) if len(clique) == 3]
    ans = 0
    for clique in cliques:
        x, y, z = clique
        if "t" in [x[0], y[0], z[0]]:
            ans += 1
            continue
    print(ans)


def part2():
    longest = max(nx.find_cliques(G), key=len)
    print(",".join(sorted(longest)))


part1()
part2()
