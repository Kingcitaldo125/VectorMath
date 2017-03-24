def is_prime(n):
    """ """
    if n<4:
        return True
    else:
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               break

#Prime number checker
num = int(input("Enter a number: "))
print(is_prime(num))
