"""FizzBuzz problem written in python."""


def fizzBuzz():
    """For loop over numbers 1 to 100 checking for multiples of 3 and 5."""
    for number in range(1, 101):
        if number % 3 == 0 & number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)


fizzBuzz()
