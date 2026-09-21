# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama: Nadine Nur’Aini  
NIM: 2225250004  
Kelas: 3B

## Tujuan

Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

Program digunakan untuk menentukan status akhir mahasiswa berdasarkan nilai ujian, nilai tugas, dan persentase kehadiran. Program melakukan validasi tipe input, validasi rentang nilai, menghitung nilai akhir dengan bobot 0.6 untuk nilai ujian dan 0.4 untuk nilai tugas, kemudian menentukan predikat dan status kelulusan.

## Cara Menjalankan

Program dijalankan melalui terminal dengan perintah:

python3 praktik/validasi_klasifikasi_nilai.py

Pada Windows, jika perintah python3 tidak dapat digunakan, dapat menggunakan:

python praktik/validasi_klasifikasi_nilai.py

Kemudian masukkan:
1. Nilai ujian dalam rentang 0 sampai 100.
2. Nilai tugas dalam rentang 0 sampai 100.
3. Persentase kehadiran dalam rentang 0 sampai 100.

## Tabel Keputusan

| Kategori | Syarat | Contoh Masukan |
|---|---|---|
| Predikat A | Nilai akhir >= 85 dan kehadiran >= 80% | Ujian 90, Tugas 80, Kehadiran 95 |
| Predikat B | Nilai akhir >= 70 dan < 85 serta kehadiran >= 80% | Ujian 75, Tugas 70, Kehadiran 85 |
| Predikat C | Nilai akhir >= 60 dan < 70 serta kehadiran >= 80% | Ujian 60, Tugas 60, Kehadiran 80 |
| Predikat D | Nilai akhir >= 50 dan < 60 serta kehadiran >= 80% | Ujian 55, Tugas 50, Kehadiran 90 |
| Predikat E | Nilai akhir < 50 dan kehadiran >= 80% | Ujian 40, Tugas 30, Kehadiran 100 |
| Tidak memenuhi syarat kehadiran | Kehadiran < 80% | Ujian 90, Tugas 90, Kehadiran 75 |
| Penolakan rentang nilai ujian | Nilai ujian < 0 atau > 100 | Ujian 105, Tugas 80, Kehadiran 90 |
| Penolakan rentang nilai tugas | Nilai tugas < 0 atau > 100 | Ujian 80, Tugas -5, Kehadiran 90 |
| Penolakan tipe | Salah satu masukan bukan angka | Ujian 80, Tugas 80, Kehadiran abc |

Nilai akhir dihitung dengan rumus:

Nilai akhir = (0.6 × nilai ujian) + (0.4 × nilai tugas)

Jika kehadiran kurang dari 80%, mahasiswa dinyatakan tidak memenuhi syarat kehadiran tanpa memandang nilai akhir.

Jika kehadiran memenuhi syarat, predikat ditentukan menggunakan rantai if-elif-else.

Predikat A, B, dan C → Lulus.

Predikat D dan E → Belum lulus.

## Hasil Pengujian

| Masukan | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| Ujian 90, Tugas 80, Kehadiran 95 | Nilai akhir 86.00, Predikat A, Lulus | Nilai akhir 86.00, Predikat A, Lulus | Berhasil |
| Ujian 75, Tugas 70, Kehadiran 85 | Nilai akhir 73.00, Predikat B, Lulus | Nilai akhir 73.00, Predikat B, Lulus | Berhasil |
| Ujian 60, Tugas 60, Kehadiran 80 | Nilai akhir 60.00, Predikat C, Lulus | Nilai akhir 60.00, Predikat C, Lulus | Berhasil |
| Ujian 55, Tugas 50, Kehadiran 90 | Nilai akhir 53.00, Predikat D, Belum lulus | Nilai akhir 53.00, Predikat D, Belum lulus | Berhasil |
| Ujian 40, Tugas 30, Kehadiran 100 | Nilai akhir 36.00, Predikat E, Belum lulus | Nilai akhir 36.00, Predikat E, Belum lulus | Berhasil |
| Ujian 90, Tugas 90, Kehadiran 75 | Nilai akhir 90.00, Tidak memenuhi syarat kehadiran | Nilai akhir 90.00, Tidak memenuhi syarat kehadiran | Berhasil |
| Ujian 105, Tugas 80, Kehadiran 90 | Penolakan rentang nilai ujian | Penolakan rentang nilai ujian | Berhasil |
| Ujian 80, Tugas -5, Kehadiran 90 | Penolakan rentang nilai tugas | Penolakan rentang nilai tugas | Berhasil |
| Ujian 80, Tugas 80, Kehadiran abc | Penolakan tipe | Penolakan tipe | Berhasil |

## Refleksi

Salah satu masukan tidak valid yang dapat terlewat adalah ketika pengguna memasukkan data yang bukan angka, misalnya `abc` pada bagian kehadiran.

Jika input langsung dikonversi menjadi float tanpa penanganan kesalahan, program akan menghasilkan `ValueError`. Untuk mengatasinya, proses konversi ketiga masukan dilindungi menggunakan `try-except ValueError`.

Dengan demikian, apabila salah satu masukan bukan angka, program dapat menolak masukan tersebut dan menampilkan pesan bahwa seluruh data harus berupa angka.