

GRAPH = {
    'start': {
        'a': 5,
        'b': 2
    },
    'a': {
        'c': 4,
        'd': 2
    },
    'b': {
        'a': 8,
        'd': 7
    },
    'c': {
        'd': 6,
        'finish': 3
    },
    'd': {
        'finish': 1
    },
    'finish': {}
}

def build_parents(graph):
    parents = {}
    for p in graph:
        for n in graph[p]:
            if n in parents:
                parents[n][p] = graph[p][n]
            else:
                parents[n] = {p: graph[p][n]}
    return parents

def build_initial_costs(graph):
    costs = {}
    for s in graph:
        for d in graph[s]:
            if s == 'start':
                costs[d] = graph[s][d]
            else:
                if d not in costs:
                    costs[d] = float("inf")
    return costs


print(build_parents(GRAPH))
print(build_initial_costs(GRAPH))
