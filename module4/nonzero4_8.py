## Write code that prompts the user to enter a number
## in the range of 1 through 100 and validates the input.


def main():
    number=int(input('Enter a number in the range of 1 through 100: '))
    while number<1 or number>100:
        print('ERROR:the number cannot be less then 1 and more then 100')
        number=int(input('Enter the correct number in the range of 1 through 100: '))  
main()
