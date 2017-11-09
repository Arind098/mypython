def is_digits(number):
    digits = []
    while number:
        digits.append(number%10)
        number //= 10
    digits.reverse()
    return digits

def is_happy(number):
    previous_num = []
    while True:
        digits = is_digits(number)
        is_sum = sum(list(map(lambda x: x **2, digits)))
        if is_sum == 1:
            return True
        elif is_sum in previous_num:
            return False
        else:
            number = is_sum
            previous_num.append(is_sum)

def main(number):
    count = 0
    happy_num = []
    while count < 8:
        if is_happy(number):
            count += 1
            happy_num.append(number)
        number += 1
    return happy_num

print (main(int(input("Enter any No."))))
