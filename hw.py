# """
# Exercise-1: is_prime
# Write a function "is_prime(n: int) -> bool" that takes an integer 'n'
# and checks whether it is prime. Function should return a boolean value.
#
# Example:
# is_prime(7) -> True
# is_prime(10) -> False
# """
#
# def is_prime(n: int) -> bool:
#     if n <= 1:
#         return  False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i+2) == 0:
#             return False
#         i+=6
#     return True
# is_prime(7) -> True
# is_prime(10) -> False

# """
# Exercise-2: nth_fibonacci
# Write a function "nth_fibonacci(n: int) -> int" that
# takes an integer 'n' and returns the nth number in the Fibonacci sequence.
#
# Example:
# nth_fibonacci(6) -> 5
# nth_fibonacci(9) -> 21
# """
#
# def nth_fibonacci(n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
# print(nth_fibonacci(6))
# print(nth_fibonacci(9))

#
# """
# Exercise-3: factorial
# Write a function "factorial(n: int) -> int" that takes an integer 'n' and returns the factorial of 'n'.
#
# Example:
# factorial(5) -> 120
# factorial(6) -> 720
# """
#
# def factorial(n: int):
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n+1):
#         result *=i
#     return result
# print(factorial(5))
# print(factorial(6))
#     pass
#
# """
# Exercise-4: count_vowels
# Write a function "count_vowels(s: str) -> int" that
# takes a string 's' and returns the number of vowels in the string.
#
# Example:
# count_vowels("hello") -> 2
# count_vowels("world") -> 1
# """
#
# def count_vowels(s: str) -> int:
#     vowels = "aeiouAEIOU"
#     result = 0
#     for char in s:
#         if char in vowels:
#             result += 1
#     return result
#
# print(count_vowels("hello"))
# print(count_vowels("world"))

#     pass
#
# """
# Exercise-5: sum_of_digits
# Write a function "sum_of_digits(n: int) -> int" that
# takes an integer 'n' and returns the sum of its digits.
#
# Example:
# def sum_of_digits(n : int):
#     n = abs(n)
#     sum_digits = 0
#     for digit in str(n):
#         sum_digits += int(digit)
#     return sum_digits
# print(sum_of_digits(12346))
# print(sum_of_digits(98766))

# """
#
#
# """
# Exercise-6: reverse_string
# Write a function "reverse_string(s: str) -> str" that takes a string 's' and returns the string reversed.
#
# Example:
# reverse_string("hello") -> "olleh"
# reverse_string("world") -> "dlrow"
# """
#
# def reverse_string(n):
#     return n[::-1]
# print(reverse_string("sayat"))
# print(reverse_string("nfactorial"))
#
#
# """
# Exercise-7: sum_of_squares
# Write a function "sum_of_squares(n: int) -> int" that takes an integer 'n' and
# returns the sum of squares of all integers from 1 to 'n'.
#
# Example:
# sum_of_squares(4) -> 30
# sum_of_squares(5) -> 55
# """
#
# def sum_of_squares(n: int) -> int:
#     # write your code here
#     pass
#
#
# """
# Exercise-8: collatz_sequence_length
# Write a function "collatz_sequence_length(n: int) -> int" that takes an
# integer 'n' and returns the length of the Collatz sequence starting with 'n'.
#
# Example:
# collatz_sequence_length(6) -> 9
# collatz_sequence_length(27) -> 112
# """
#
# def collatz_sequence_length(n: int):
#     count = 1
#     while n != 1:
#         if n % 2 == 0:
#            n = n // 2
#         else: n = n * 3 + 1
#         count += 1
#     return count
#
# print(collatz_sequence_length(6))
# print(collatz_sequence_length(27))
#
#
# """
# Exercise-9: is_leap_year
# Write a function "is_leap_year(year: int) -> bool" that takes an
# integer 'year' and returns True if 'year' is a leap year, and False otherwise.
#
# Example:
# is_leap_year(2000) -> True
# is_leap_year(1900) -> False
# """
#
# def is_leap_year(year: int):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 ==0:
#         return True
#     else:
#         return False
#
# print(is_leap_year(2000))
# print(is_leap_year(1900))
#
#
# """
# Exercise-10: count_words
# Write a function "count_words(s: str) -> int" that takes a string 's' and
# returns the number of words in the string. Assume words are separated by spaces.
#
# Example:
# count_words("Hello world") -> 2
# count_words("This is a test") -> 4
# """
#
# def count_words(s: str):
#     words = s.split()
#     return len(words)
#
# print(count_words("Hello world"))
# print(count_words("This is a test sayat is nfactorials best"))
#
# """
# Exercise-11: is_palindrome
# Write a function "is_palindrome(s: str) -> bool" that takes a string 's' and
# checks if the string is a palindrome. The function should return True if the
# string is a palindrome, and False otherwise.
#
# Example:
# is_palindrome("racecar") -> True
# is_palindrome("hello") -> False
# """
#
# def is_palindrome(s: str) -> bool:
#     if s == s[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome("racecar"))
# print(is_palindrome("hello"))
# write your code here
#     pass
#
# """
# Exercise-12: sum_of_multiples
# Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that
# takes three integers 'n', 'x', and 'y', and returns the sum of all the
# numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.
#
# Example:
# sum_of_multiples(10, 3, 5) -> 33
# sum_of_multiples(20, 7, 11) -> 168
# """
#
# def sum_of_multiples(n:int, x:int, y:int):
#     count = 0
#     for num in range(1,n+1):
#         if num % x == 0 or num % y ==0:
#             count += num
#     return count
# print(sum_of_multiples(10, 3, 5))  # Ожидаемый результат: 33
# print(sum_of_multiples(20, 7, 11)) # Ожидаемый результат: 168 <- здесь поидее 32 получиться
#
#
# """
# Exercise-13: gcd
# Write a function "gcd(a: int, b: int) -> int" that takes two integers 'a' and 'b',
# and returns their greatest common divisor (GCD).
#
# Example:
# gcd(56, 98) -> 14
# gcd(27, 15) -> 3
# """
#
# def gcd(a: int, b: int) -> int:
#     while b != 0:
#         a, b = b, a % b
#     return a
# print(gcd(56, 98))
# print(gcd(27, 15))

#
#
# """
# Exercise-14: lcm
# Write a function "lcm(a: int, b: int) -> int" that takes two integers 'a' and 'b',
# and returns their least common multiple (LCM).
#
# Example:
# lcm(5, 7) -> 35
# lcm(6, 8) -> 24
# """
#
# def lcm(a: int, b: int) -> int:
#     while b != 0:
#         a, b = b, a % b
#     return a
# print(lcm(5, 7))
# print(lcm(6, 8))
#
#
# """
# Exercise-15: count_characters
# Write a function "count_characters(s: str, c: str) -> int" that
# takes a string 's' and a character 'c', and returns the number of occurrences of 'c' in 's'.
#
# Example:
# count_characters("hello world", "l") -> 3
# count_characters("apple", "p") -> 2
#
#
# """
#
# def count_characters(s: str, c: str) -> int:
#     return s.count(c)
# print(count_characters("hellllllo world", "l"))
# print(count_characters("applepp", "p"))

#     # write your code here
#     pass
#
#
# """
# Exercise-16: digit_count
# Write a function "digit_count(n: int) -> int" that takes an
# integer 'n' and returns the number of digits in 'n'.
#
# Example:
# digit_count(123) -> 3
# digit_count(4567) -> 4
# """
#
# def digit_count(n: int):
#     return len(str(abs(n)))
# print(digit_count(123))
# print(digit_count(456789))
#
#
# """
# Exercise-17: is_power_of_two
# Write a function "is_power_of_two(n: int) -> bool" that takes an integer 'n'
# and returns True if 'n' is a power of 2, and False otherwise.
#
# Example:
# is_power_of_two(8) -> True
# is_power_of_two(10) -> False
# """
#
# def is_power_of_two(n: int) -> bool:
#     return n > 0 and (n &(n - 1)) == 0
#
# print(is_power_of_two(8))
# print(is_power_of_two(10))
#
#
# """
# Exercise-18: sum_of_cubes
# Write a function "sum_of_cubes(n: int) -> int" that takes an integer 'n'
# and returns the sum of the cubes of all numbers from 1 to 'n'.
#
# Example:
# sum_of_cubes(3) -> 36
# sum_of_cubes(4) -> 100
# """
#
# def sum_of_cubes(n: int) -> int:
#     # write your code here
#     pass
#
#
# """
# Exercise-19: is_perfect_square
# Write a function "is_perfect_square(n: int) -> bool" that takes an
# integer 'n' and returns True if 'n' is a perfect square, and False otherwise.
#
# Example:
# is_perfect_square(9) -> True
# is_perfect_square(10) -> False
# """
#
# def is_perfect_square(n: int) -> bool:
#     # write your code here
#     pass
#
#
# """
# Exercise-20: is_armstrong_number
# Write a function "is_armstrong_number(n: int) -> bool" that takes an
# integer 'n' and returns True if 'n' is an Armstrong number, and False otherwise.
#
# Example:
# is_armstrong_number(153) -> True
# is_armstrong_number(370) -> True
# """
#
# def is_armstrong_number(n: int) -> bool:
#     # write your code here
#     pass
