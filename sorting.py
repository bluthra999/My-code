
import random
# MONKEY SORT aka	bogosort,	stupid	sort, slowsort,	permutaAon	sort,	shotgun	sort
# Principle : Randomly sort till the list becomes sorted
def bogo_sort(L):
    while L != sorted:
        random.shuffle(L)
        print(L, end=":")
        print(sorted)

testList = [1,3,5,7,2,6,25,18,13]
sorted = sorted(testList)
print(sorted)
bogo_sort(testList)
print(testList)




def bubble_sort(L):
    '''swap is used to flag if we have had to swap any elements of the array'''
    sort = False # we set swap to True here before the inner loop starts
    while not sort:
        print('bubble sort: ' + str(L))
        sort = True # if no swaps have been done then the value of swap is never changed and 
       # when the inner loop finishes the value of swap will still be True#
       
        for j in range(1, len(L)): #Swaps the elements #
            
            if L[j-1] > L[j]:
                sort = False
                temp = L[j]
              
                L[j] = L[j-1]   # stores the value in L[j-1] in L[j]#
                L[j-1] = temp

testList = [1,3,5,7,2,6,25,18,13]

print('')
print(bubble_sort(testList))
print(testList)


def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)): #i always start from a newsuffixSt whenever the if cond is not met
            if L[i] < L[suffixSt]:#if condition is not met , i += 1
                L[suffixSt], L[i] = L[i], L[suffixSt] 
        suffixSt += 1
 
testList = [3,2,1]
       
print('')
print(selection_sort(testList))
print(testList)


def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
        
testList = [1,3,5,7,2,6,25,18,13]

#print('')
#print(merge_sort(testList))

