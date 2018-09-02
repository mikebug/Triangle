##Michael Buglione
##I plegde my honor that I abided by the stevens honors system.



def classify_triangle(a,b,c):
    a, b, c = sorted([a, b, c])
    r =""
    if abs(a * a + b * b - c * c) < 0.1:
        r = "Right"
    if a == b and b == c:
        s = "Equilateral"
    elif a == b or b == c or a == c:
        s = "Isosceles"
    else:
        s = "Scalene"
    if not isnumber(a) or not isnumber(b) or not isnumber(c) or a <= 0 or b <= 0 or c <= 0:
        s = ("NotATriangle")
        return s
    return s + ' ' + r


def isnumber(a):
        if type(a) == int or type(a) == float:
            return True


print (classify_triangle(2,2,2))
print (classify_triangle(5,1,1))
print (classify_triangle(5,4,3))
print (classify_triangle(0,0,0))
