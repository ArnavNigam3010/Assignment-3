def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter a number: "))
print("Factorial of number is: ",factorial(n))