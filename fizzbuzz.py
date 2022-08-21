# start by creating a for loop
# create a variable (numbers in this example, but can be whatever you want)
# use the range function to go through numbers 1-100

for number in range(1, 101):
    # if number is divisible by 3 AND 5 the word FIZZBUZZ will be printed.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # if number is divisible by 5 the word BUZZ is printed.
    elif number % 5 == 0:
        print("Buzz")
    # if number is divisible by 3 the word FIZZ is printed.
    elif number % 3 == 0:
        print("Fizz")
    # if number isn't divisible by 3, 5, or both then the number is printed out.
    else:
        print(number)