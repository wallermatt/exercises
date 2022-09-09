

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

def get_lowest_unprocessed_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = ""
    for n in costs:
        if n in processed:
            continue
        if costs[n] < lowest_cost:
            lowest_cost_node = n
            lowest_cost = costs[n]
    return lowest_cost_node

def update_costs(costs, parents, node):
    for p in parents:
        if node in parents[p]:
            new_cost = costs[node] + parents[p][node]
            if costs[p] > new_cost:
                costs[p] = new_cost


def get_lowest_path(graph):
    parents = build_parents(graph)
    costs = build_initial_costs(graph)
    processed = []
    while len(processed) < len(graph) - 1:
        n = get_lowest_unprocessed_node(costs, processed)
        update_costs(costs, parents, n)
        processed.append(n)
    return costs


print(get_lowest_path(GRAPH))

'''
print(build_parents(GRAPH))
print(build_initial_costs(GRAPH))

parents = build_parents(GRAPH)
costs = build_initial_costs(GRAPH)
n = get_lowest_unprocessed_node(costs, [])
print(n)

update_costs(costs, parents, 'b')
print(costs)
'''