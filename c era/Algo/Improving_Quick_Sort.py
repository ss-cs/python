# Uses python3
import sys
import random


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a.sort()
    for i in a:
        print(i,end=" ")
