import cmath
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))

d=(b**2)-(4*a*c)

d1=(-b+cmath.sqrt(d))/2*a
d2=(-b-cmath.sqrt(d))/2*a

print(d1)
print(d2)

print('The solution are {0} and {1}'.format(d1,d2))
