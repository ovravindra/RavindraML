# search element by element as the algoorithm runs through out the data set

def bruteForce(test, searchItem):
    found = False
    for i in test:
        if i == searchItem:
            found = True
            break
        else: found = False
    return found