# To swap two variables

a = input("Enter variable a value: ")
print("a =", a)
b = input("Enter variable b value: ")
print("b =", b)

temp_var = a
a = b
b = temp_var

# a, b = b, a

print("a variable after swapping:", a)
print("b variable after swapping:", b)
