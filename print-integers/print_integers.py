# Print the list of integers from  through  as a string, without spaces.
from __future__ import print_function

if __name__ == '__main__':
    n = int(input("Enter a number: "))

    for i in range(1, n+1):
        print(i, end='')