print ("selamat datang diprogram biodata")
print ("================================")

# buka file
file_lagu = open("lagu.txt", "r")
teks = file_lagu.read()
# cetak isi file
print (teks)
# Ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")
# format teks
teks ="Nama : {}\nUmur: {}\nAlamat: {}\n".format(nama, umur, alamat)
# bukan file untuk ditulis
file_bio = open("biodata.txt", "a")
# tulis teks file
file_bio.write(teks)
# tutup file
file_bio.close()