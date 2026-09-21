a = float(input("Masukkan sudut pertama: "))
b = float(input("Masukkan sudut kedua: "))
c = float(input("Masukkan sudut ketiga: "))

if a + b + c != 180:
    print("Bukan segitiga.")
elif a == 90 or b == 90 or c == 90:
    print("Segitiga siku-siku.")
elif a > 90 or b > 90 or c > 90:
    print("Segitiga tumpul.")
else:
    print("Segitiga lancip.")