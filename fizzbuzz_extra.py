import sys
my_input=input("Harry Kwong")
try:
    for n in range(1, int(sys.argv[1])):
        if n % 3 == 0 + n % 5 == 0: print("FizzBuzz")
        elif n % 3 == 0: print("Fizz")
        elif n % 5 == 0: print("Buzz")
        else: print(n)
    
except IndexError:
    print(my_input)
        




        