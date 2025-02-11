def main():
    run_loop='No'
    while run_loop == 'No':
        print("This program adds two numbers. ")
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        total = num1 + num2
        print("{} + {} = {}".format(num1, num2, total))
        run_loop = input("Do you want to end the program?")
        print("come back again to add more Numbers")
if __name__ == "__main__":
    main()
