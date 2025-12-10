def binary_search(vector, target):
    lower_bound = 0
    upper_bound = len(vector)
    found = False
    i = 0
    while found == False and i<len(vector):
        midpoint = (upper_bound+lower_bound)//2
        if vector[midpoint] == target:
            found = True
            return True
        if vector[midpoint] <= target:
            lower_bound = midpoint
        if vector[midpoint] >= target:
            upper_bound = midpoint
        i += 1
    return False

for i in range(10):
    print(i, binary_search([1,4,7,8,9,10,1573,9008], i))