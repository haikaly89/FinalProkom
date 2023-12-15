import time
import os

 
def pertanyaan():
    while True:  
        makanan = input("Masukkan makanan yang ingin di cek: ")
        poin = 0

        pertanyaan_list = [
            "1. Apakah makananmu mengandung nasi, roti, atau kentang? (iya/tidak): ",
            "2. Apakah makananmu mengandung daging, ikan, telur, atau susu? (iya/tidak): ",
            "3. Apakah makananmu mengandung sayur-sayuran atau buah-buahan? (iya/tidak): ",
            "4. Apakah makananmu tidak terlalu berminyak atau berlemak? (iya/tidak): ",
            "5. Apakah makananmu tidak terlalu manis atau asin? (iya/tidak): ",
            "6. Apakah makananmu bersih dan tidak basi? (iya/tidak): ",
            "7. Apakah makananmu sesuai dengan porsi yang kamu butuhkan? (iya/tidak): ",
            "8. Apakah makananmu berbeda-beda setiap hari? (iya/tidak): ",
            "9. Apakah makananmu enak dan membuatmu senang? (iya/tidak): ",
            "10. Apakah makananmu ada di dalam piramida makanan sehat? (iya/tidak): "
        ]

        for pertanyaan_text in pertanyaan_list:
            jawaban = input(pertanyaan_text)
            if jawaban.lower() == "iya":
                poin += 1

        if poin >= 7:
            print(f"{makanan} adalah makanan yang sehat dengan poin {poin}. Anda dapat mengonsumsinya secara teratur.")
        else:
            print(f"{makanan} adalah makanan yang tidak sehat dengan poin {poin}.")

    
        back = input("Apakah anda ingin cek makanan lagi ? (y/n) ")

        if back == "n":
            print("="*35, "\n")
            print('Program telah berakhir, anda akan kembali ke menu utama')
            time.sleep(4)
            os.system('cls')
            break