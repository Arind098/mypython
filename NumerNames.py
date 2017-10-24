units = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
teens = ['','Eleven','Twelve','Thirteen','Forteen','Fifteen','Sixteen','Seventeen','Eightteen','Nineteen']
tens = ['','Ten','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
thousands = ['','Thousand','Million','Billion','Trillion','Quadrillion','Quitillion','Sextillion']
#############################################################################
#### A list can be considered with Units,Teens,Tens and Thousands in it #####
#############################################################################
lst = []
num = int(input ("Enter any number: "))
while num > 0:
    lst.append(num%1000)
    num //=1000
lst.reverse()
def main():
    hun = ''
    for count in range(len(lst)):
        if lst[count] > 0:
            hun += hundred(lst[count])+' '+thousands[len(lst)-1-count] +' '
        elif lst[count] == 0:
            continue
    return hun

def hundred(num1):
    words = ''
    if num1 < 10:
        words = units[num1]
    elif num1 > 10 and num1 < 20:
        words = tens[num1%10]
    elif num1 == 10 or num1 > 20 and num1 < 100:
        words = tens[num1//10]+units[num1%10]
    elif num1 >= 100:
        if num1%100 > 20:
            words = units[num1//100]+' Hundred'+' '+tens[int(str(num1)[1])]+' '+units[num1%10]
        if num1%100 < 20:
            words = units[num1//100]+' Hundred'+' '+teens[int(str(num1)[1])]+' '+units[num1%10]
    return words

main()
