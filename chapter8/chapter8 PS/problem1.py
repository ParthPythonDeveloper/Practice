# Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a = 15
b = 56
c = 10

print(greatest(a, b, c))