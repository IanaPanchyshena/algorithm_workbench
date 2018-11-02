# Write a while loop that asks the user to enter two numbers.
# The numbers should be added and the sum displayed.
# The loop should ask the user if he or she wishes
# to perform the operation again.
# If so, the loop should repeat, otherwise it should terminate. 


def main():
    total=0
    keep_going='y'

    while keep_going=='y':
        print('Enter two numbers for total:')
        number1=int(input('Enter number: '))
        number2=int(input('Enter number: '))
        total=number1+number2
        print('Total is' , total)
        keep_going=input('Do you want to perform operation again?'
                         'Enter "y" for Yes: ')
main()
    
