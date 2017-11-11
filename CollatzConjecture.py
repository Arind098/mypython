def is_even(num):
    return num//2

def is_odd(num):
    return (3*num)+1

def main():
    num = int(input("Enter any num: "))
    count = 0
    while num != 1:
        if num%2 == 0:
            num = is_even(num)
        else:
            num = is_odd(num)
        count +=1
    print (count)
main()
