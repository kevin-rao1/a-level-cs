# 17 list comprehension problems in python
import math

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
output = [fruit.upper() for fruit in fruits]
print(output)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]. Hint: Use <string>.capitalize()
output = [fruit.capitalize() for fruit in fruits]
print(output)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (sum(1 for ch in fruit.lower() if ch in 'aeiou')) > 2] # counts characters that are vowels in each item, with thanks to some random stackoverflow user from 11 years ago
print(fruits_with_more_than_two_vowels) # good opportunity to use regex instead?

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if (sum(1 for ch in fruit.lower() if ch in 'aeiou')) == 2] # adapted from above

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_chars = [fruit for fruit in fruits if (sum(1 for ch in fruit)) > 5]
print(fruits_with_more_than_five_chars)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_only_five_chars = [fruit for fruit in fruits if (sum(1 for ch in fruit)) == 5]
print(fruits_with_only_five_chars)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_chars = [fruit for fruit in fruits if (sum(1 for ch in fruit)) < 5]
print(fruits_with_less_than_five_chars)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
list_of_number_of_characters_in_each_fruit = [sum(1 for ch in fruit) for fruit in fruits]
print(list_of_number_of_characters_in_each_fruit)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
list_of_number_of_characters_in_each_fruit = [fruit for fruit in fruits if fruit.find("a") > -1]
print(list_of_number_of_characters_in_each_fruit)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number%2 == 0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number%2 == 1]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numbers_with_2_or_more_numerals = [number for number in numbers if len(str(abs(number))) >= 2] # counts length of number as str, but without the "-"
print(numbers_with_2_or_more_numerals)
# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number**2 for number in numbers]
print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number%2 == 1 and number < 0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [number+5 for number in numbers]
print(numbers_plus_5)
print("My autocomplete broke")

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
""" this is too readable
# Compute sieve of Eratosthenes, see https://stackoverflow.com/questions/46460127/efficiently-finding-prime-numbers-in-python
# this took about as long as the rest of the exercise
limit = max(numbers)
sieve = [2]
for i in range(3, limit+1):
    for j in sieve:
        if i % j == 0:
            break
    else:
        sieve.append(i)
primes = [number for number in numbers if number in sieve]"""
# an incomprehensible list comprehension for the previous, optimised™
primes = [number for number in numbers if number in [n for n in range(2, max(numbers)+1) if all(n % d for d in range(2, int(n**0.5)+1))]]
print(primes)