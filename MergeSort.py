def splitting(aList):
    mid = len(aList)//2
    if len(aList) > 1:
        firstHalf = aList[:mid]
        splitting(firstHalf)
        secHalf = aList[mid:]
        splitting(secHalf)
        sorting(aList,firstHalf,secHalf)
    
def sorting(newList,a,b):
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            newList[k] = a[i]
            i += 1
        else:
            newList[k] = b[j]
            j += 1
        k += 1
        
    while i < len(a):
        newList[k] = a[i]
        i += 1
        k += 1
            
    while j < len(b):
        newList[k] = b[j]
        j += 1
        k += 1
aList = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
splitting(aList)
print (aList)
