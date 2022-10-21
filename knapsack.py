'''
EXERCISE
9.2 Suppose you’re going camping. You have a knapsack that will hold
6 lb, and you can take the following items. Each has a value, and the
higher the value, the more important the item is:
• Water, 3 lb, 10
• Book, 1 lb, 3
• Food, 2 lb, 9
• Jacket, 2 lb, 5
• Camera, 1 lb, 6
What’s the optimal set of items to take on your camping trip?
'''
ITEMS = [
    ['water',3,10],
    ['book',1,3],
    ['food',2,9],
    ['jacket',2,5],
    ['camera',1,6],
]

SIZE = 6

def fill_knapsack():
    # loop through items - rows i
    # loop through 1 to 6 (size) - columns j
    # build table
    # same column row above OR item + i-1, j-item size
    knapsack = [[0 for j in range(SIZE)] for i in range(len(ITEMS))]
    for i, row in enumerate(knapsack):
        item = ITEMS[i]
        name = item[0]
        weight = item[1]
        value = item[2]
        for j, column in enumerate(row):
            if i:
                column_above = knapsack[i-1][j]
            else:
                column_above = 0
            
            current_value = 0
            if j+1 == weight:
                current_value = value
            elif j+1 > weight:
                current_value = value
                if i:
                    current_value += knapsack[i-1][j-weight]

            if column_above > current_value:
                knapsack[i][j] = column_above
            else:
                knapsack[i][j] = current_value
    return knapsack


k = fill_knapsack()

for i, row in enumerate(k):
    print(ITEMS[i], row)



