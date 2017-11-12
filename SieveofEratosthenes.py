num = int(input("Enter any no.: "))
aList = [i for i in range(2,num+1)]
for k in aList:
    for j in range(2,len(aList)):
        try:
            aList.remove(k*j)
        except ValueError:
            continue
print ("The Prime nos. upto the no.%r"%num + " is \n",aList)
