# Bisection search
# Only works for sorted list
# Order : O(Log(n))

def bisect_search2(L, e):
    '''e is the element you want to find , L is the list in which you want to find e'''
    def bisect_search_helper(L, e, low, high):
        print('low: ' + str(low) + '; high: ' + str(high))  #added to visualize
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

testList = []
for i in range(11):
    testList.append(i)
    
print(bisect_search2(testList, 10))


# Linear search 
# Only works for sorted list
# Order : O(n) but on avg  is faster than alternate method

def search(L, e):
    '''e is the element you want to find , L is the list in which you want to find e'''
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# Alternate Linear search 
# Works for both sorted and unsorted list
# Order : O(n)

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
