# This is a simple calculation program
# created to demonstrate version control.
from libadd import *
from libmult import *
a = 13
b = 5
print(plus(a,b))
print(mult(a,b))
print(multx(a,b,2))

def divide_numbers(a, b):
    """
    Funkcija, kas dala divus skaitļus.
    Ja dalītājs (b) ir 0, atgriež kļūdas paziņojumu.
    """
    if b == 0:
        return "Kļūda: Dalīšana ar 0 nav atļauta!"
    return a / b

# Piemērs, kā izmantot funkciju
if __name__ == "__main__":
    print("Dalīšanas rezultāts:", divide_numbers(12, 4))
