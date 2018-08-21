#using generator
def fib():
    first,second = 1,1
    while True:
        yield first
        first,second = second, first+second
n = 0

for i in fib():
    if n >= 10 :
        break;
    print (i)
    n += 1
    

