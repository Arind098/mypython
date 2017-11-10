def is_digits(num):
  digits = []
  while num:
    digits.append(num%10)
    num //= 10
  digits.reverse()
  return digits

def checksum(num):
  new = []
  digits = is_digits(num//10)
  digits_2nd = [i * 2 for i in digits[::-2]]
  digits_2nd.reverse()
  for x in digits_2nd:
    if x > 9:
      new.append(x//10 + x%10)
    else:
      new.append(x)
  return sum(new)

def main():
  card_no = int(input("Enter any Credit Card No, to Validate"))
  if 10 - (int(str(checksum(card_no))[-1])) == card_no%10:
    print ("Entered card is Valid")
  else:
    print ("Entered credit card no. is invalid")

main()
