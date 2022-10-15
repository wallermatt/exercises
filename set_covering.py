'''
1. need to cover full set
2. take option that covers most remaining elements
3. repeat
'''

UNIVERSE = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})

OPTIONS = {
    'a': set({1,2,3}),
    'b': set({3,4}),
    'c': set({5,1}),
    'd': set({6}),
    'e': set({7}),
    'f': set({8}),
    'g': set({9}),
    'h': set({10}),
    'i': set({1,4,7,10}),
    'j': set({5,9}),
    'k': set({9,10}),
}

remaining = UNIVERSE
selected = []

while remaining:
    max_len = 0
    best_option = None
    for o in OPTIONS:
        if o in selected:
            continue
        if len(OPTIONS[o]&remaining) > max_len:
            best_option = o
            max_len = len(OPTIONS[o]&remaining)
    remaining = remaining.difference(OPTIONS[best_option])
    print(best_option, remaining)
    selected.append(best_option)

print(selected)
    


