nilai = input("Masukkan nilai akhir (0-100): ")

try:
    nilai = float(nilai)

    if nilai < 0 or nilai > 100:
        print("Error: nilai harus berada pada rentang 0-100.")
    elif nilai >= 85:
        print(f"Nilai {nilai:.2f} memperoleh predikat A.")
    elif nilai >= 70:
        print(f"Nilai {nilai:.2f} memperoleh predikat B.")
    elif nilai >= 60:
        print(f"Nilai {nilai:.2f} memperoleh predikat C.")
    elif nilai >= 50:
        print(f"Nilai {nilai:.2f} memperoleh predikat D.")
    else:
        print(f"Nilai {nilai:.2f} memperoleh predikat E.")

except ValueError:
    print("Error: input harus berupa angka.")