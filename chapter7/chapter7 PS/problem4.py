# Write a program to find whether a given number is prime or not.

n = int(input("Enter number: "))
for i in range(2, n):
    if(n%1) == 0:
        print("Number is not prime")
        break
else:
        print("Number is prime")

        