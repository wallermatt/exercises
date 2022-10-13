'''
at each step take the local optimum solution

classes - start and end
maximise number of classes held

classes = {
    'english': (1,3),
    'french': (1,2),
    'maths': (2,3),
    'cs': (2,4),
    'history': (3,4),
    'geography': (3,5),
    'RE': (4,5),
}

'''

# build start times
# get subject that finished earliest that starts at time (or closest)
# remove start time from start times
# have initial start time



class Class:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __eq__(self, other):
        if self.name == other.name and self.start == other.start and self.end == other.end:
            return True
        return False
    
    def __str__(self):
        return str(self.name) + ", " + str(self.start)  + ", " + str(self.end)


def get_shortest_class(classes, start):
    shortest_class = None
    for c in classes:
        if not shortest_class and c.start == start:
            shortest_class = c
        elif not shortest_class:
            continue
        if c.start == start and c.end < shortest_class.end:
            shortest_class = c
    return shortest_class


def schedule(classes, start=1):
    schedule = []
    while classes:
        next_class = get_shortest_class(classes, start)
        schedule.append(next_class)
        start = next_class.end
        classes = [c for c in classes if c.start >= start]
    return schedule
    
#print(schedule([Class('english',1,3)], 1))
assert schedule([Class('english',1,3)], 1) == [Class('english',1,3)]
