def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, num):
        if num % i == 0:
            return False  # Not a prime number if divisible by any number other than 1 and itself
    return True  # If no divisors are found, it's a prime number

def main():
    num = 12
    if is_prime(num):
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number.")

main()