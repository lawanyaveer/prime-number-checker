#prime number checker
#100 days python bootcamp
#8th day




def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it is a prime no.")
    else:
        print("its not a prime number")


number = int(input("check this number : "))
prime_checker(number )