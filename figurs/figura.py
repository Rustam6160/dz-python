import cmath
import math
def triangle(a, b, c):
    perimetr = a + b+ c
    p = (a + b+ c) /2
    ploshad= math.sqrt(p * (p -a)*(p-b)*(p-c))

    print(f"периметр треугольника=  {perimetr} площадь треугольника= {ploshad} ")

def kvadrat(a):
    perimetr = a*4
    ploshad = a * a
    print(f"периметр квадрата=  {perimetr} площадь квадрата= {ploshad}")

def pryamaugolnik(a, b):
    perimetr = a*2 + b*2
    ploshad= a * b
    print(f"периметр прямоугольника=  {perimetr} площадь прямоугольника= {ploshad}")

def krug(r):
    dlina_okruzhnost = 2*r*math.pi
    S = math.pi * r**2
    print(f"длина окружности= {dlina_okruzhnost} площадь= {S}")

def trapecia(a, b, c, d):
    P = a+b+c+d
    S = (a+b)/2 * math.sqrt(c**2 - (((a-b)**2 +c**2 - d**2)/ (2*(a-b)))**2)
    print(f"периметр трапеции= {P} площадь трапеции= {S}")

triangle(1.5, 1.5, 1.5,)
kvadrat(2)
pryamaugolnik(2, 4)
krug(3)
trapecia(9, 5,  8, 6)