from utils import square, is_even, celsius_to_fahrenheit, greet


name = input("Enter your name: ")
print(greet(name))

number = int(input("Enter a number: "))

print(f"Square: {square(number)}")

if is_even(number):
    print("The number is even.")
else:
    print("The number is odd.")

fahrenheit = celsius_to_fahrenheit(number)
print(f"Fahrenheit: {fahrenheit}")