
print("=== APLIKASI PERHITUNGAN GAJI KARYAWAN ===")

hari_kerja           = int(input("Masukkan Jumlah Hari Kerja Karyawan       : "))
hari_kerja_perbulan  = 30      # Jumlah hari kerja per bulan
gaji_pokok           = 10000000
tarif_lembur_per_jam = 50000  # Misalnya tarif lembur per jam adalah Rp 50.000
jam_lembur           = int(input("Masukkan Jumlah Jam Lembur yang Dilakukan : ")) # Jumlah jam lembur yang dilakukan karyawan

# Menghitung total gaji pokok
total_gaji_pokok = (hari_kerja / hari_kerja_perbulan) * gaji_pokok

# Menghitung total gaji lembur
total_gaji_lembur = jam_lembur * tarif_lembur_per_jam

# Menghitung total gaji keseluruhan
total_gaji = total_gaji_pokok + total_gaji_lembur

# Mengonversi total gaji menjadi string dengan tanda pemisah
total_gaji_string = "{:,.2f}".format(total_gaji)

# Menampilkan total gaji dengan tanda pemisah
print("Total Gaji Keseluruhan   : Rp.", total_gaji_string)



