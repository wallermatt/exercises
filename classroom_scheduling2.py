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


def build_shortest_class_dict(classes):
    shortest_classes = {}
    max_start = 0
    for c in classes:
        if c.start > max_start:
            max_start = c.start
        if c.start in shortest_classes:
            existing_class = shortest_classes[c.start]
            if (c.end - c.start) < (existing_class.end - existing_class.start):
                shortest_classes[c.start] = c
        else:
            shortest_classes[c.start] = c
    return shortest_classes, max_start
    

def get_shortest_class(shortest_classes, start):
    if start in shortest_classes:
        return shortest_classes[start]
    else:
        return None


def schedule(classes, start=1):
    schedule = []
    shortest_classes, max_start = build_shortest_class_dict(classes)
    while start <= max_start:
        next_class = None
        while not next_class:
            next_class = get_shortest_class(shortest_classes, start)
            if not next_class:
                start += 1
        schedule.append(next_class)
        start = next_class.end
    return schedule
    

#print(schedule([Class('english',1,3)], 1))
assert schedule([Class('english',1,3)], 1) == [Class('english',1,3)]
assert schedule([Class('english',1,3), Class('french',1,2)], 1) == [Class('french',1,2)]
assert schedule([Class('english',2,3), Class('french',1,2)], 1) == [Class('french',1,2), Class('english',2,3)]

assert schedule([Class('english',2,3)], 1) == [Class('english',2,3)]

assert schedule([Class('english',1,2), Class('french',2,3), Class('welsh',2,4), Class('esperanto',3,4)], 1) == [Class('english',1,2), Class('french',2,3), Class('esperanto',3,4)]

