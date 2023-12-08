def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(start, end):
    if start < 0:
        print("Enter a non-negative number.")
        return
    if end <= start:
        print(f"Enter a number greater than {start}.")
        return

    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)


while True:
    start = int(input("Enter a number [start]: "))

    if start == 0:
        print("Program terminated.")
        break

    end = int(input("Enter a number [end]: "))

    display_primes(start, end)