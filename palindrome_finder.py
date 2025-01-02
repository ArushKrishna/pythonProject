
def next_palindrome(number):
  number += 1
  while str(number) != str(number)[::-1]:
      number += 1
  return number


input_number = int(input("Enter a positive integer up to 20 digits: "))
if len(str(input_number)) < 8:
  print("The next palindrome is:", next_palindrome(input_number))
else:
  num = str(input_number)
  len_num = len(num)
  if len_num % 2 == 0:
      first_half = num[:len_num//2]
      second_half = num[len_num//2:]
      second_half = first_half[::-1]
      next_pal = first_half + second_half
      if int(next_pal) < input_number:
          next_pal = str(int(first_half) + 1) + (str(int(first_half) + 1))[::-1]
      print(next_pal)
  else:
      first_half = num[:len_num//2]
      second_half = num[len_num//2:]
      middle = second_half[0]
      second_half = first_half[::-1]
      while int(f"{first_half}{middle}{second_half}") <= input_number:
          middle = str(int(middle) + 1)
          if int(middle) > 9:
              middle = str(int(middle) % 10)
              first_half = str(int(first_half) + 1)
              second_half = first_half[::-1]
      print(first_half + middle + second_half)
