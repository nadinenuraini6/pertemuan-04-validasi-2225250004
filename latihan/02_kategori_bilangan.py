bilangan = int(input("Masukkan bilangan bulat: "))

if bilangan > 0:
    kategori = "positif"
elif bilangan < 0:
    kategori = "negatif"
else:
    kategori = "nol"

print(f"Bilangan {bilangan} termasuk {kategori}.")