def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b 

def multiplication(a,b):
    return a*b   

def division(a,b):
    if (b!=0):
        return a/b

    else:
        print("Error")
        return None

def truncated_division(a,b):
    if(b != 0):
        return a//b

    else:
        print("Error")
        return None

def modulus(a,b):
    if(b != 0):
        return a % b

    else:
        print("Error")
        return None

def exponentiation(a,b):
    return a**b

a = 10 
b = 3

print("Addition:",addition(a,b))
print("Subtraction:",subtraction(a,b))
print("Multiplication:",multiplication(a,b))
print("Division:",division(a,b))
print("Truncated division:",truncated_division(a,b))
print("Modulus:",modulus(a,b))
print("exponentiation:",exponentiation(a,b))