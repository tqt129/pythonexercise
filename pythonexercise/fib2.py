#fib using sequence
def fib(n):
    first,second = 0, 1
    for i in range(n-1):
        first, second = second, first+second
    return first
for i in range(1,10):
    print (fib(i))
