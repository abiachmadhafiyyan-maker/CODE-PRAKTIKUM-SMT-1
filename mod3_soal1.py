jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

print("--- Program Kasir Bus Terminal Sidoarjo ---")
print("Masukkan jarak tempuh (ketik 0 untuk berhenti)")

while True:
    jarak = float(input("Masukkan jarak (km): "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid!")
        continue

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    jumlah_penumpang += 1

    if jumlah_penumpang % 5 == 0:
        tarif *= 0.5
        print(f"Penumpang ke-{jumlah_penumpang} dapat diskon 50%!")

    total_pendapatan += tarif
    total_jarak += jarak
    jarak_terjauh = max(jarak_terjauh, jarak)

print("\nLAPORAN AKHIR")

if jumlah_penumpang > 0:
    print(f"Jumlah penumpang : {jumlah_penumpang} orang")
    print(f"Total pendapatan : Rp{total_pendapatan}")
    print(f"Jarak terjauh    : {jarak_terjauh} km")
    print(f"Rata-rata jarak  : {total_jarak / jumlah_penumpang} km")
else:
    print("Tidak ada data penumpang.")