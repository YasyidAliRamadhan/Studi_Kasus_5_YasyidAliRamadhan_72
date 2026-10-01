
def hitung_biaya(jenis_kendaraan, lama_parkir):

    if jenis_kendaraan == "Mobil":
        tarif = 7000
    elif jenis_kendaraan == "motor":
        tarif = 3000

    total_biaya = tarif * lama_parkir
    return total_biaya

#input data
jenis_kendaraan = input("Masukkan jenis kendaraan: ")
jam_masuk = int(input("Masukkan jam masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))

#mengitung lama parkir
lama_parkir = jam_keluar - jam_masuk

total_biaya = hitung_biaya(jenis_kendaraan, lama_parkir)

#hasil
print("\n===DATA PARKIR===")
print("Jenis kendaraan :", jenis_kendaraan)
print("Jam masuk       :", jam_masuk)
print("Jam keluar      :", jam_keluar)
print("Lama parkir     :", lama_parkir, "jam")
print("total biaya     :Rp", total_biaya)