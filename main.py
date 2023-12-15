import time
import os
import menu 

import dataresep
import bmi
import manualcheck
import autocheck
 
def main():
    while True :
        menu.menu()
        print ("="*40)
        pilihan_program = input("Masukan kode pilihan anda : ")
        print ("="*40)
        if pilihan_program == "1" :
            manualcheck.pertanyaan()

        elif pilihan_program == "2" :
            bmi.cek_bmi()
            
        elif pilihan_program == "3" :
            dataresep.pilihanresep()
  
        elif pilihan_program == "4" :
            autocheck.thisFood()

        elif pilihan_program == "99" :
            print ("Program telah berakhir. Terimakasih!")
            exit ()
        else : 
            print ("Masukkan kode dengan benar!")
            time.sleep(1)
            os.system('cls')

main()