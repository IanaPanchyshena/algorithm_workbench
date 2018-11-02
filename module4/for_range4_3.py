# Write a for loop that displays the following
# set of numbers: 0, 10, 20, 30, 40, 50 . . . 1000 

def main():
    for number in range(0,1001,10):
        print(format(number,'8d'),end='')
main()
