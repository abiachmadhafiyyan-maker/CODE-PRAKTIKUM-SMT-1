jumlah_penerima = 0

for i in range(1, 11):
    print("\n--- Mahasiswa ke-" + str(i) + " ---")
    nama = input("Nama: ")
    ipk = float(input("IPK (contoh: 3.25): "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat (IPK di bawah 3.00)")
        continue

    penghasilan = float(input("Penghasilan orang tua per bulan (Rp): "))

    if penghasilan <= 3000000:
        print("Hasil:", nama, "mendapat Beasiswa Penuh")
        jumlah_penerima += 1
    elif penghasilan <= 5000000:
        print("Hasil:", nama, "mendapat Beasiswa Sebagian")
        jumlah_penerima += 1
    else:
        print("Hasil:", nama, "tidak mendapat beasiswa")

    if jumlah_penerima == 3:
        print("\nKuota beasiswa (3 orang) sudah terpenuhi.")
        break

print("\nSELESAI SELEKSI")
print("Jumlah penerima beasiswa:", jumlah_penerima, "dari 3 kuota")