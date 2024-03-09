# Recursion function hi hote hai,
# agar same function ke andar dubara uss function ko call krte h to usse recursion bolte h
def factorial (num):
    if (num==0 or num ==1):
        return 1
    else:
        return num*factorial(num-1)

#num=int(input("Enter the number:"))
print(factorial(10))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return n+(n-1)
print(fibonacci(3))
