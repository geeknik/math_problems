#The Collatz conjecture is a conjecture in mathematics that states that for any positive integer n, the following process always reaches 1:

#If n is even, divide it by 2.
#If n is odd, multiply it by 3 and add 1.
#The conjecture is named after Lothar Collatz, who introduced the idea in 1937.

def collatz(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    print(n)
collatz(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
