import random
import time

#Experiment One
def inList():
    bin_count = 0
    bin_total = 0
    tri_count = 0
    tri_total = 0
    for j in range (250, 80000, 3000): #number of values in the list, changes by 3000 
        lis = []
        k = []
        for i in range (0, j):
            num = random.randint(0, 1000000)
            lis.append(num)#adds random nums between 0-1,000,000
            if i%10 == 0:  #searches for every 10th element
                k.append(num)

        lis = qsort(lis, 0, len(lis)-1)

        print "Experiment #1"
        
        start = time.time()
        for q in k: #searches for every element in k
            bin_search(lis, 0, len(lis)-1, q)
        fin = time.time()
        print "Binary Search took ", (fin-start), " time with ", j, "elements in the list, searching for ", len(k)
        bin_total += fin-start

        start_two = time.time()
        for w in k: #searches for every element in k
            trin_search(lis, 0, len(lis)-1, w)
        fin_two = time.time()
        print "Trinary Search took ", (fin_two-start_two), " time with ", j, "elements in the list, searching for ", len(k)
        tri_total += fin_two-start_two
        
        if ((fin-start) > (fin_two-start_two)):
            print "Trinary search was faster"
            tri_count += 1
        else:
            print "Binary search was faster"
            bin_count += 1
        print ""
    print "Trinary was faster ", tri_count, " times"
    print "Binary was faster ", bin_count, " times"
    print "Binary Total: ", bin_total
    print "Trinary Total: ", tri_total
        
#Experiment Two
def notInList():
    bin_count = 0
    tri_count = 0
    for j in range (250, 80000, 3000):#number of values in the list, changes by 3000
        lis = []
        k = []
        for i in range (0, j):
            num = random.randrange(0, 2000000, 2)
            lis.append(num)#adds random even numbers up to 2 million
            if i%10 == 0: #adds number to k after every 10 numbers
                k.append(num-1) #searches for the number below the even num in list

        lis = qsort(lis, 0, len(lis)-1)

        print "Experiment #2"
        
        start = time.time()
        for q in k:
            bin_search(lis, 0, len(lis)-1, q)
        fin = time.time()
        print "Binary Search took ", (fin-start), " time with ", j, "elements in the list, searching for ", len(k)

        start_two = time.time()
        for w in k:
            trin_search(lis, 0, len(lis)-1, w)
        fin_two = time.time()
        print "Trinary Search took ", (fin_two-start_two), " time with ", j, "elements in the list, searching for ", len(k)
        if ((fin-start) > (fin_two-start_two)):
            print "Trinary search was faster"
            tri_count += 1
        else:
            print "Binary search was faster"
            bin_count += 1
        print ""
    print "Trinary was faster ", tri_count, " times"
    print "Binary was faster ", bin_count, " times"


def qsort(lis, l, r):
    i = l
    j = r
    p = lis[l + (r - l) / 2] 
    while i <= j:
        while lis[i] < p: i += 1
        while lis[j] > p: j -= 1
        if i <= j:  
            lis[i], lis[j] = lis[j], lis[i]
            i += 1
            j -= 1
    if l < j: 
        qsort(lis, l, j)
    if i < r: 
        qsort(lis, i, r)
    return lis          

def bin_search(lis,first,last,target):
    if first > last:
        return -1
    else:
        mid = (first+last)/2
        if mid >= len(lis): 
            return -1
        if lis[mid] == target:
            return mid
        elif lis[mid] > target:
            return bin_search(lis,first,mid-1,target)
        else:
            return bin_search(lis,mid+1,last,target)



def trin_search(lis,first,last,target):
    if first > last:
        return -1
    else:
        one_third = first + (last-first)/3
        if one_third >= len(lis): 
            return -1
        two_thirds = first + 2*(last-first)/3
        if two_thirds >= len(lis): 
            return -1
        if lis[one_third] == target:
            return one_third
        elif lis[one_third] > target:
            return trin_search(lis,first,one_third-1,target)
        elif lis[two_thirds] == target:
            return two_thirds
        elif lis[two_thirds] > target:
            return trin_search(lis,one_third+1,two_thirds-1,target)
        else:
            return trin_search(lis,two_thirds+1,last,target)



    

