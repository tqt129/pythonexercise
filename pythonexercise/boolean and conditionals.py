"""Create a program that asks the user how far they want to travel. If they want to travel less than
three miles tell them to walk. If they want to travel more than three miles, but less than three
hundred miles, tell them to drive. If they want to travel three hundred miles or more tell them to
fly.
"""
while True:
    try:
        ask = (input("how far do you want to travel: "))
        ask = int(ask)
        if ask <= 3:
            mode_of_transport = 'walking'
        elif ask <= 100:
            mode_of_transport = 'driving'
        elif ask > 100:
            mode_of_transport = 'flying'
        print('I suggest {} to your destination.'.format(mode_of_transport))
    except :
        if ask == 'ten':
            print("ten ten ten")
        elif ask == 'quit':
            exit()
        else:
            print("invalid option")

