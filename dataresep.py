import os
import time


#===========================================================================================
def listresep(): 
    print ("="*35)
    print ( "Pilih resep yang ingin ada lihat\n")
    print ("1. Smoothie Buah-buahan Segar") 
    print ("2. Wrap Sayuran dengan Daging Ayam Panggang") 
    print ("99. Keluar")  
    print ("="*35, "\n")


#===========================================================================================
def smuti ():
    print (""" 
╔════════════════════════════════════════════════════════════╗
║               Smoothie Buah-buahan Segar                   ║
╚════════════════════════════════════════════════════════════╝
                                                             ║
🍌 Bahan:                                                    
- Pisang matang                                              ║
- Beberapa stroberi (bisa diganti dengan buah-buahan lain)   ║
- Yogurt tanpa gula                                          ║
- Air secukupnya                                             ║
                                                             ║
👩‍🍳 Cara membuat:                                             
1. Potong pisang dan stroberi menjadi potongan kecil.        ║
2. Masukkan potongan buah ke dalam blender.                  ║
3. Tambahkan yogurt sesuai selera.                           ║
4. Tuangkan air secukupnya.                                  ║
5. Blender semua bahan hingga halus dan konsisten.           ║
6. Sajikan dalam gelas dan nikmati segera.                   ║
                                                             ║
╔════════════════════════════════════════════════════════════╗
║                    Selamat mencoba!                        ║
╚════════════════════════════════════════════════════════════╝

""")
    

#===========================================================================================
def tortil ():
    print (""" 
╔════════════════════════════════════════════════════════════╗
║         Wrap Sayuran dengan Daging Ayam Panggang           ║
╚════════════════════════════════════════════════════════════╝
                                                             ║
🌮Bahan:                                                    
- Tortilla gandum                                            ║
- Dada ayam (dipanggang dan potong dadu)                     ║
- Daun selada                                                ║
- Tomat (potong dadu)                                        ║
- Saus sambal atau saus pilihan Anda                         ║
                                                             ║
👩‍🍳 Cara membuat:                                             
1. Letakkan selembar tortilla di atas permukaan datar.       ║ 
2. Tata daun selada, potongan daging ayam, dan potongan      ║
   tomat di tengah-tengah tortilla.                          ║
3. Teteskan saus sambal atau saus pilihan Anda di atas isian.║
4. Lipat tepi kiri dan kanan tortilla ke tengah, lalu gulung ║
   dari bawah ke atas hingga membentuk wrap.                 ║
5. Sajikan dan nikmati.                                      ║
                                                             ║
╔════════════════════════════════════════════════════════════╗
║                    Selamat mencoba!                        ║
╚════════════════════════════════════════════════════════════╝

""")

#===========================================================================================

def pilihanresep () :
    listresep()
    while True :
        pilihan = input("Pilih resep yang ingin anda lihat : ")

        if pilihan == "1":
            smuti ()
        elif pilihan == "2":
            tortil()
        else :
            print ("Masukkan kode sesuai dengan list! ")

        back = input("Apakah anda ingin lihat resep lainnya? (y/n) ")
        if back == "n":
            print("="*35, "\n")
            print('Program telah berakhir, anda akan kembali ke menu utama')
            time.sleep(4)
            os.system('cls')
            break 