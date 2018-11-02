# Write a loop that asks the user to enter a number.
# The loop should iterate 10 times
# and keep a running total of the numbers entered.

def main():
    total=0
    num=int(input('enter num: '))
    for number in range (1,11):
        new=num*number
        total=total+new
        print(number,'\t',new)
    print('Total is',total)
main()
    
