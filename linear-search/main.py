def linear_search(vector, element):
    for item in vector:
        if item == element:
            return True
    return False

if linear_search([5,6,9008], 7) == True:
    print("aaa")