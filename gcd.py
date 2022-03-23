a = int(input("Enter a = "))
b = int(input("Enter b = "))

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)




print("GCD value: ",gcd(a,b))