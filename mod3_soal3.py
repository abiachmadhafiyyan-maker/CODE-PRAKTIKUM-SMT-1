jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai = 0
tertinggi = -1
nama_tertinggi = ""
terendah = 101
nama_terendah = ""

for i in range(1, 11):
    print("\n--- Mahasiswa ke-" + str(i) + " ---")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas (0-100): "))
    uts = float(input("Nilai UTS (0-100): "))
    uas = float(input("Nilai UAS (0-100): "))

    nilai_akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    print("Hasil:", nama, "| Nilai akhir:", round(nilai_akhir, 2), "| Kategori:", kategori)

    total_nilai += nilai_akhir

    if nilai_akhir > tertinggi:
        tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < terendah:
        terendah = nilai_akhir
        nama_terendah = nama

print("\n--- RINGKASAN KELAS ---")
print("Rata-rata nilai akhir :", round(total_nilai / 10, 2))
print("Nilai tertinggi       :", round(tertinggi, 2), "(" + nama_tertinggi + ")")
print("Nilai terendah        :", round(terendah, 2), "(" + nama_terendah + ")")

print("\nJumlah mahasiswa per kategori:")
print("Kategori A (85 - 100) :", jumlah_A, "orang")
print("Kategori B (75 - 84)  :", jumlah_B, "orang")
print("Kategori C (65 - 74)  :", jumlah_C, "orang")
print("Kategori D (50 - 64)  :", jumlah_D, "orang")
print("Kategori E (< 50)     :", jumlah_E, "orang")