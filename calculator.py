#calculator

s = input("Enter char +, -, *, /, ** :")


#a = int(input("Enter num A:"))
#b = int(input("Enter num B:"))

if s == "+":
    a = int(input("Enter num A:"))
    b = int(input("Enter num B:"))
    c = a + b
elif s == "-":
    a = int(input("Enter num A:"))
    b = int(input("Enter num B:"))
    c = a - b

elif s == "*":
    a = int(input("Enter num A:"))
    b = int(input("Enter num B:"))
    c = a * b
elif s == "/":
    a = int(input("Enter num A:"))
    b = int(input("Enter num B:"))
    c = a / b
if s == "**":
    a = int(input("Enter num A:"))
    c = a ** a
else:
    print("is not")

print("Result:" + str(c))
