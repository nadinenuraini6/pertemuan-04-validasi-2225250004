try:
    nilai = float(input("Masukkan nilai: "))
    print(f"Input valid: {nilai}")
except ValueError:
    print("Input tidak valid. Masukkan angka.")