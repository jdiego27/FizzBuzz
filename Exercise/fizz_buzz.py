# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”

def fizz():
    for numero in range(1,101):
        if numero % 15 == 0:
            print('FizzBuzz')
        elif numero % 3 == 0:
            print('Fizz')
        elif numero % 5 == 0:
            print('Buzz')
        else:
            print(numero)

fizz()
