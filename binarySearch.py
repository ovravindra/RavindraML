# Search through the sorted algorithm by dividing it in half. and repeating the division till the element is found.

def binarySearch(test, searchitem):

    len1 = len(test)
    if len1 >= 1:
        mid = len1//2
        middle_element = test[mid]
        if (searchitem == middle_element):
            return True
        elif searchitem < middle_element:
            list1 = test[ :mid]
            return binarySearch(list1, searchitem)
        elif searchitem > middle_element:
            list1 = test[mid+1: ]
            return binarySearch(list1, searchitem)
        
    return False




test0 = [-3, 1, 3, 9, 11, 14, 22, 123, 302, 304, 434, 501, 1230, 5412, 381923]
searchItem0 = 13
print(binarySearch(test0, searchItem0))
 
test1 = [1, 7, 9, 12, 22, 43, 104]
searchItem1 = 9
print(binarySearch(test1, searchItem1))
 
test2 = [-20, -5, 0, 0, 30, 100]
searchItem2 = 31
print(binarySearch(test2, searchItem2))
 
test3 = [4, 17, 28, 30, 52, 61, 666, 1001]
searchItem3 = 666
print(binarySearch(test3, searchItem3))

