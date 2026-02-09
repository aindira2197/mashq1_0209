# 1
ism = input("Ismingizni kiriting: ")
print(f"Salom, {ism}! Python dunyosiga xush kelibsiz!")

# 2
yil = int(input("Tug‘ilgan yilingizni kiriting: "))
print(2026 - yil)

# 3
son = int(input("Raqam kiriting: "))
print("Juft" if son % 2 == 0 else "Toq")

# 4
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))

# 5
tanlov = input("C yoki F: ").upper()
qiymat = float(input())
if tanlov == "C":
    print((qiymat * 9/5) + 32)
else:
    print((qiymat - 32) * 5/9)
