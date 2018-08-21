import sys
def Fibonacci(n):
    if n <=1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def start():
  try:
    userinput = raw_input("enter the nth term of the sequence or type 'ten' to see the ten sequence or 'quit': ")
    if userinput == ('ten'):
        for i in range(1,10):
            print(Fibonacci(i))
    elif userinput == ('quit'):
        sys.exit()
    else:
       newinput = int(userinput)
       print(Fibonacci(newinput))
  except ValueError:
      print("invalid entry")
while True:
 start()
