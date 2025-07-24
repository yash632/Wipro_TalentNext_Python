# 1. Write a function to return the sum of all numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20

def sum_list(numbers):
    return sum(numbers)

print(sum_list([8, 2, 3, 0, 7]))

# 2. Write a function to return the reverse of a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"

def reverse_string(s):
    return s[::-1]

print(reverse_string("1234abcd"))

# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
# 4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count_case(s):
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

count_case("Hello World")
# 5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]

def even_numbers(lst):
    result = [x for x in lst if x % 2 == 0]
    print(result)

even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))