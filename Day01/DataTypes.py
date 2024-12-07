# in DataType are specify type of data store in variable

#1) Numeric Types=============================================================>

#int: Represents whole numbers>>>>>>>>.
age = 2545454  # Integer example
print(age)
print(type(age)) #can see type
print(age.__sizeof__())

num= -25
print(num)

#float: Represents numbers with decimal points>>>>>>>>>.
pi = 3.14159  # Float example
print(pi)

#complex: Represents complex numbers, with a real and imaginary part>>>.
z = 3 + 4j  # Complex number
print(z)
print(z.real)

#2) Boolean type================================================================>
a=True
print(a)
b=False
print(b)
print("\"\"\"\"\"\"\"")

#******In Python convert between different numeric data types*****************
x=234
a=float(x)
print(x)

_float_new=3434.3433434
_convert_int=int(_float_new)
print(_convert_int)

_convert_complex=complex(x)
print(_convert_complex)
