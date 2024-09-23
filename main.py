# Function to check if a number is prime
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# # Input: Number to check
# num = int(input("Enter a number: "))

# # Output: Prime or not
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

print("welcome to my weird detector application")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is not a prime number.")
elif number % 2 == 0:
    print(f"{number} is a prime number ") 

else:
    print("odd number")    


