import random

angka = random.randint(1,10)
print ("#" * 40)
print ('   Kamu Bisa Menebak Angka Dari 1/10.\n    Dan Kamu Memiliki 3x Kesempatan')
print("#" * 40)

batas_percobaan = 3

for percobaan in range (batas_percobaan) :
	jawaban = int(input(f"\n [percobaan {percobaan + 1}] Masukkan Angka Tebakanmu : "))
	if jawaban == angka:
		print('Selamat Kamu Benar')
		break
	else:
		print('Tebakanmu Terlalu' , 'Kecil' if jawaban < angka else 'Besar')

else :
	print(f'\nSayang Sekali Kamu Sudah Salah Menebak Sebanyak {batas_percobaan}x!')