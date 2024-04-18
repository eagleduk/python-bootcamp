def prime_checker(number):
    i = 2
    while number % i != 0:
        i += 1

    if i == number:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input())
prime_checker(number=n)