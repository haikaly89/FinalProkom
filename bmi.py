import os
import time


def cek_bmi():
    while True:
        gender = input("Masukkan jenis kelamin (pria/wanita): ").lower()

        if gender == "pria":
            berat_badan = float(input("Masukkan berat badan anda : "))
            tinggi_badan = float(input("Masukkan tinggi badan anda : "))

            tinggi_badan = tinggi_badan / 100
            bmi = berat_badan / (tinggi_badan**2)

            if bmi < 17:
                hasil = "Anda kekurangan berat badan tingkat berat! tolong makan makanan yang bergizi!"
            elif 17 <= bmi < 18.5:
                hasil = "Anda kekurangan berat badan tingkat ringan! tolong makan makanan yang bergizi!"
            elif 18.5 <= bmi <= 25:
                hasil = "Berat badan anda normal! tolong dipertahankan!"
            elif 25.1 <= bmi <= 27:
                hasil = "Anda kelebihan berat badan tingkat ringan! tolong kurangi berat anda secara berkala!"
            elif bmi > 27:
                hasil = "Anda kelebihan berat badan tingkat berat! tolong kurangi berat anda secara berkala!"

            print(f"BMI anda adalah : {bmi:.2f}, {hasil}")

        elif gender == "wanita":
            berat_badan = float(input("Masukkan berat badan anda : "))
            tinggi_badan = float(input("Masukkan tinggi badan anda : "))

            tinggi_badan = tinggi_badan / 100
            bmi = (berat_badan) / (tinggi_badan**2)

            if bmi < 17:
                hasil = "Anda kekurangan berat badan tingkat berat! tolong makan makanan yang bergizi!"
            elif 17 <= bmi < 18.5:
                hasil = "Anda kekurangan berat badan tingkat ringan! tolong makan makanan yang bergizi!"
            elif 18.5 <= bmi <= 25:
                hasil = "Berat badan anda normal! tolong dipertahankan!"
            elif 25.1 <= bmi <= 27:
                hasil = "Anda kelebihan berat badan tingkat ringan! tolong kurangi berat anda secara berkala!"
            elif bmi > 27:
                hasil = "Anda kelebihan berat badan tingkat berat! tolong kurangi berat anda secara berkala!"

            print(f"BMI anda adalah : {bmi:.2f}, {hasil}")

        else :
            print ("Tolong masukkan sesuai dengan pilihan!")

    
        back = input("Apakah anda ingin cek BMI lagi ? (y/n) ")
        if back == "n":
            print("="*35, "\n")
            print('Program telah berakhir, anda akan kembali ke menu utama')
            time.sleep(4)
            os.system('cls')
            break