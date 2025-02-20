def main():
  stop_loop = "no"
  while stop_loop != "yes":
   print("Hi im going to convert decimal to binary to binary to decimal")
   num = input ("Enter binary number")
   binary_num = binary_to_decimal(num)
   print("Binary {} to Decimal: {}". format(num, binary_num) )
   decimal_input = int(input("Enter a decimal number: "))
   binary_output = decimal_to_binary(decimal_input)
   print("Binary representation:", binary_output)
   stop_loop = input("Type 'yes' to exit program: ").lower().strip()
def binary_to_decimal(number):
   result = 0
   if len(number) > 0:
       power = len(str(number)) - 1 # determine greatest power
       for num in str(number):
           result += int(num) * 2 ** power
           power -= 1 # decrease by 1
       return result
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary_string = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_string = str(remainder) + binary_string
        decimal_num //= 2
    return binary_string

if __name__ == "__main__":
    main()
