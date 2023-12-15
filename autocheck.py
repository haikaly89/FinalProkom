import time
import os



healthy_foods = ["nasi putih", "jagung", "ayam",
 "almond", "oat", "keju", "yoghurt", "susu", "brokoli", "udang",
 "rumput laut", "cumi", "singkong", "tuna", "jahe", "kunyit", "apel",
 "gudeg", "capcay", "bawang bombay", "tempe", "tahu", "kentang", "pisang",
 "bayam", "ikan bawal", "karedok", "daun kasbi", "pepaya", "buah kelor",
 "daun pepaya", "sayur asem", "sayur lebui", "nanas", "ubi cilembu",
 "nasi merah", "salak", "bebek", "ikan nila", "gado-gado", "selada",
 "kacang panjang", "daun bawang merah", "kacang merah", "kacang hijau",
 "papeda", "ikan lele", "ikan patin", "ubi jalar", "ikan baronang",
 "jeruk", "kangkung", "asparagus", "kubis", "daging kelinci"]

unhealthy_foods = ["daging merah", "gorengan", "keripik", "es krim", "cokelat",
 "rendang", "soto", "martabak", "bakso", "mie goreng", "hotdog", "jeroan", "daging olahan",
 "sosis", "daging berlemak", "sate", "pempek", "siomay", "risoles", "pastel", "lumpia", "nasi goreng",
 "seblak", "cilok", "corndog", "saus kemasan", "onde-onde", "bika ambon", "brownies", "batagor",
 "mi instan", "sarden kalengan", "brownies", "crepes", "nugget ayam", "popcorn caramel",
 "kacang goreng", "biskuit", "asinan", "kue lapis", "ayam goreng", "bubble milk tea", "bakso aci", "waffle"]

nutrition_data = {
    "nasi putih" : {"kalori": 180, "protein": 1.9, "lemak": 12, "karbohidrat": 0, "serat": 0},
    "jagung" : {"kalori": 142, "protein": 5, "lemak": 0.7,  "karbohidrat": 30, "serat": 0.8},
    "ayam" : {"kalori": 165, "protein": 31, "lemak": 3.6, "karbohidrat": 0, "serat": 0},
    "tahu" : {"kalori ": 76, "protein ": 8, "lemak ": 5, "karbohidrat ": 2, "serat": 1},
    "almond" : {"kalori ": 579, "protein ": 21, "lemak ": 50, "karbohidrat ": 22, "serat ": 12.5},
    "oat" : {"kalori ": 389, "protein": 17, "lemak ": 7, "karbohidrat ": 66, "serat ": 11},
    "keju" : {"kalori ": 402, "protein ": 25, "lemak ": 33, "karbohidrat ": 1.3, "serat ": 0},
    "yoghurt" : {"kalori ": 59, "protein ": 10, "lemak ": 0.4, "karbohidrat ": 3.6, "serat ": 0},
    "susu" : {"kalori ": 42, "protein ": 3.4, "lemak ": 1, "karbohidrat ": 5, "serat ": 0},
    "brokoli" : {"kalori ": 34, "protein ": 2.8, "lemak ": 0.4, "karbohidrat ": 7, "serat ": 2.6},
    "udang" : {"kalori ": 99, "protein ": 24, "lemak ": 0.3, "karbohidrat ": 0.2, "serat ": 0},
    "rumput Laut" : {"kalori ": 45, "protein ": 38, "lemak ": 1, "karbohidrat ": 10, "serat ": 2.2},
    "cumi" : {"kalori ": 92.4, "protein ": 16.3, "lemak ": 1.4, "karbohidrat ": 2.6, "Serat ": 0},
    "singkong" : {"kalori ": 154, "protein ": 1, "lemak ": 0, "karbohidrat ": 36.9, "serat ": 0},
    "tuna" : {"kalori ": 144, "protein ": 23, "lemak ": 5, "karbohidrat ": 0, "serat ": 0},
    "jahe" : {"kalori ": 80, "protein ": 1.8, "lemak ": 0.8, "karbohidrat ": 18, "serat ": 2},
    "kunyit" : {"kalori ": 354, "protein ": 7.8, "lemak ": 10, "karbohidrat ": 65, "serat ": 21},
    "apel" : {"kalori ": 52, "protein ": 0.3, "lemak ": 0.2, "karbohidrat ": 14, "serat ": 24},
    "gudeg" : {"kalori ": 160, "protein ": 3.3, "lemak ": 9.2, "karbohidrat ": 16, "serat ": 2.3},
    "capcay" : {"kalori ": 97, "protein ": 4.8, "lemak ": 6.3, "karbohidrat ": 4.2, "serat ": 0.6},
    "bawang bombay" : {"kalori ": 43, "protein ": 1.4, "lemak ": 0.2, "karbohidrat ": 10.3, "serat ": 2},
    "tempe" : {"kalori ": 192, "protein ": 19, "lemak ": 11, "karbohidrat ": 9, "serat ": 8},
    "tahu" : {"kalori ": 76, "protein": 8, "lemak ": 5, "karbohidrat ": 2, "serat ": 1},
    "kentang" : {"kalori ": 77, "protein ": 2, "lemak ": 0.1, "karbohidrat ": 17, "serat ": 2.2},
    "pisang" : {"kalori ": 89, "protein ": 1.1, "lemak ": 0.3, "karbohidrat ": 23, "serat ": 26},
    "daging merah" : {"kalori ": 300, "protein ": 26, "lemak ": 20, "karbohidrat ": 0, "serat ": 0},
    "gorengan" : {"kalori ": 300, "protein ": 4, "lemak ": 20, "karbohidrat ": 30, "serat ": 2},
    "keripik" : {"kalori ": 152, "protein ": 2, "lemak ": 9.8, "karbohidrat ": 14, "serat ": 1.1},
    "es krim" : {"kalori ": 207, "protein ": 3.5, "lemak ": 11, "karbohidrat ": 24, "serat" : 0.8},
    "cokelat" : {"kalori ": 546, "protein ": 7.6, "lemak ": 31, "karbohidrat ": 61, "serat ": 3.3},
    "rendang" : {"kalori ": 195, "protein ": 19, "lemak ": 9, "karbohidrat ": 9, "serat ": 1.8},
    "soto" : {"kalori ": 285, "protein ": 18, "lemak ": 14, "karbohidrat ": 23, "serat ": 12.5},
    "martabak" : {"kalori ": 650, "protein ": 16, "lemak ": 40, "karbohidrat ": 60, "serat ": 2},
    "bakso" : {"kalori ": 342, "protein ": 17, "lemak ": 25, "karbohidrat ": 13, "serat ": 1.5},
    "mie goreng" : {"kalori ": 383, "protein ": 9, "lemak ": 19, "karbohidrat ": 47, "serat ": 3},
    "sosis" : {"kalori ": 190, "protein ": 20, "lemak ": 8, "karbohidrat ": 12, "serat ": 0},
    "hotdog" : {"kalori ": 189, "protein ": 7, "lemak ": 17, "karbohidrat ": 1.8, "serat ": 0},
    "jeroan" : {"kalori ": 200, "protein ": 20, "lemak ": 15, "karbohidrat ": 5, "serat ": 0},
    "daging olahan" : {"kalori ": 300, "protein ": 20, "lemak ": 15, "karbohidrat ": 5, "serat ": 0},
    "daging berlemak" : {"kalori ": 300, "protein ": 26, "lemak ": 20, "karbohidrat ": 0, "serat ": 0},
    "sate" : {"kalori ": 197, "protein ": 17, "lemak ": 10, "karbohidrat ": 9, "serat ": 1},
    "pempek" : {"kalori ": 165, "protein ": 8, "lemak ": 7, "karbohidrat ": 19, "serat ": 1},
    "siomay" : {"kalori ": 215, "protein ": 11, "lemak ": 9, "karbohidrat ": 25, "serat ": 2},
    "risol" : {"kalori ": 165, "protein ": 5, "lemak ": 9, "karbohidrat ": 18, "serat ": 1},
    "pastel" : {"kalori ": 160, "protein ": 4, "lemak ": 8, "karbohidrat ": 19, "serat ": 1},
    "lumpia" : {"kalori ": 133, "protein ": 4, "lemak ": 6, "karbohidrat ": 16, "serat": 1},
    "nasi goreng" : {"kalori ": 358, "protein ": 8, "lemak ": 14, "karbohidrat ": 52, "serat ": 2},
    "seblak" : {"kalori ": 262, "protein ": 8.15, "lemak ": 13, "karbohidrat ": 31, "serat ": 0},
    "cilok" : {"kalori ": 266, "protein ": 2.4, "lemak ": 2.5, "karbohidrat ": 58, "serat ": 0.8},
    "corndog" : {"kalori ": 263, "protein ": 9.6, "lemak ": 10.8, "karbohidrat ": 32, "serat ": 0},
    "saus kemasan" : {"kalori ": 35, "protein ": 1, "lemak ": 2, "karbohidrat ": 8, "serat ": 1},
    "minuman kemasan" : {"kalori ": 140, "protein ": 0, "lemak ": 0, "karbohidrat ": 39, "serat ": 0},
    "sarden kalengan" : {"kalori ": 110, "protein ": 12, "lemak ": 2, "karbohidrat ": 9, "serat ": 0},
    "onde-onde" : {"kalori ": 90, "protein ": 2, "lemak ": 3, "karbohidrat ": 15, "serat ": 1},
    "bika ambon" : {"kalori ": 160, "protein ": 3, "lemak ": 5, "karbohidrat ": 27, "serat ": 0},
    "brownies" : {"kalori ": 180, "protein ": 3, "lemak ": 9, "karbohidrat ": 24, "serat ": 1},
    "batagor" : {"kalori ": 220, "protein ": 10, "lemak " : 10, "karbohidrat ": 26, "serat ": 2},
    "mi instan" : {"kalori ": 420, "protein ": 9, "lemak ": 16, "karbohidrat ": 64, "serat ": 3},
    "bayam" : {"kalori ": 16, "protein ": 0.9, "lemak ": 0.4, "karbohidrat ": 2.9, "serat ": 0.7},
    "ikan bawal" : {"kalori ": 91, "protein ": 19, "lemak ": 1.7, "karbohidrat ": 0, "serat ": 0},
    "karedok" : {"kalori ": 92, "protein ": 2.2, "lemak ": 3.3, "karbohidrat ": 14, "serat ": 1.4},
    "daun kasbi" : {"kalori ": 92, "protein ": 4, "lemak ": 3.6, "karbohidrat ": 11, "serat ": 5.8},
    "pepaya" : {"kalori ": 46, "protein ": 0.5, "lemak ": 0.1, "karbohidrat ": 12.2, "serat ": 1.6},
    "buah kelor" : {"kalori ": 38, "protein ": 1.5, "lemak ": 0.1, "karbohidrat ": 7.5, "serat ": 3.2},
    "daun pepaya" : {"kalori ": 87, "protein ": 8, "lemak ": 2, "karbohidrat ": 12, "serat ": 1.5},
    "sayur asem" : {"kalori ":29, "protein ": 0.7, "lemak ": 0.6, "karbohidrat ": 5, "serat ": 0.6},
    "sayur lebui" : {"kalori ": 64, "protein ": 2.1, "lemak ": 0.6, "karbohidrat": 12.5, "serat ": 5.7},
    "nanas" : {"kalori " : 40, "protein ": 0.6, "lemak ": 0.3, "karbohidrat": 10, "serat": 0.6},
    "ubi cilembu" : {"kalori ": 186, "protein ": 1.9, "lemak ": 0.2, "karbohidrat": 44, "serat ": 3.4},
    "nasi merah" : {"kalori ": 149, "protein ": 2.8, "lemak ": 0.4, "karbohidrat ": 32.5, "serat ": 0.3},
    "salak" : {"kalori ": 87, "protein ": 0.8, "lemak ": 0.4, "karbohidrat ": 20, "serat ": 0},
    "bebek" : {"kalori ": 321, "protein ": 16, "lemak ": 28, "karbohidrat ": 0, "serat ": 0},
    "ikan nila" : {"kalori ": 96, "protein ": 20, "lemak ": 1.7, "karbohidrat ": 0, "serat ": 0},
    "gado-gado" : {"kalori ": 137, "protein ": 6.1, "lemak ": 3.2, "karbohidrat ": 21, "serat ": 1.1},
    "selada" : {"kalori ": 18, "protein ": 1.2, "lemak ": 0.2, "karbohidrat ": 2.9, "serat ": 1.8},
    "kacang panjang" : {"kalori ": 31, "protein ": 2.3, "lemak ": 0.1, "karbohidrat ": 5.3, "serat ": 2.7},
    "daun bawang merah" : {"kalori ": 41, "protein ": 2, "lemak ": 0, "karbohidrat ": 7.8, "serat ": 2.1},
    "kacang merah" : {"kalori ": 350, "protein ": 13.9, "lemak ": 3, "karbohidrat ": 67, "serat ": 0},
    "kacang hijau" : {"kalori ": 109, "protein ": 8.7, "lemak ": 0.5, "karbohidrat ": 18.3, "serat ": 1.5},
    "papeda" : {"kalori ": 61, "protein ": 0.2, "lemak ": 0.1, "karbohidrat ": 15, "serat ": 0.5},
    "ikan lele" : {"kalori ": 92, "protein ": 16.2, "lemak ": 2.82, "karbohidrat ": 0, "serat ": 0},
    "ikan patin" : {"kalori ": 142, "protein ": 17, "lemak ": 6.6, "karbohidrat ": 1.1, "serat ": 0},
    "ikan baronang" : {"kalori ": 78, "protein ": 14.5, "lemak ": 0.6, "karbohidrat ": 3.7, "serat ": 0},
    "ubi jalar" : {"kalori ": 119, "protein ": 0.5, "lemak " :0.4, "karbohidrat": 25.1, "serat": 4.20},
    "jeruk" : {"kalori ": 45, "protein ": 0.9, "lemak ": 0.2, "karbohidrat ": 11.2, "serat ": 1.4},
    "kangkung" : {"kalori ": 28, "protein ": 3.4, "lemak ": 0.7, "karbohidrat ": 3.9, "serat ": 2},
    "asparagus" : {"kalori ": 20, "protein ": 2.2, "lemak ": 0.12, "karbohidrat ": 3.88, "serat ": 2.10},
    "kubis" : {"kalori ": 51, "protein ": 2.5, "lemak ": 1.1, "karbohidrat ": 8, "serat ": 3.4},
    "daging kelinci" : {"kalori ": 142, "protein ": 16.9, "lemak ": 7.8, "karbohidrat ": 0, "serat ": 0},
    "nugget ayam" : {"kalori ": 489, "protein ": 35.8, "lemak ": 29.2, "karbohidrat ": 25.6, "serat ": 0.8},
    "popcorn caramel" : {"kalori": 498, "protein": 4.1, "lemak ": 29.2, "karbohidrat ": 60.6, "serat": 0.8},
    "kacang goreng" : {"kalori": 564, "protein": 25.5, "lemak ": 44.4, "karbohidrat ": 25.5, "serat ": 0},
    "biskuit" : {"kalori ": 50, "protein ": 2, "lemak ": 5, "karbohidrat ": 10, "serat ": 1},
    "asinan" : {"kalori ": 200, "protein ": 5, "lemak ": 10, "karbohidrat ": 20, "serat ": 5},
    "kue lapis" : {"kalori ": 300, "protein ": 5, "lemak ": 15, "karbohidrat ": 30, "serat ": 2},
    "ayam goreng" : {"kalori ": 215, "protein ": 22.9, "lemak ": 12.28, "karbohidrat ": 0, "serat ": 0},
    "bubble milk tea" : {"kalori ": 160, "protein ": 3, "lemak ": 6, "karbohidrat ": 27, "serat ": 0.4},
    "bakso aci" : {"kalori ": 218, "protein ": 2, "lemak ": 1.9, "karbohidrat ": 48.8, "serat ": 0},
    "waffle" : {"kalori ": 581, "protein ": 5, "lemak": 17, "karbohidrat ": 5, "serat ": 0},
}

def print_nutrition(food):
    print(f"Data nutrisi untuk {food}:")
    print("-" * 40)
    print(f"{'Nutrien':<20}{'Jumlah':<10}{'Satuan':<10}")
    print("-" * 40)
    # Menampilkan data nutrisi untuk setiap nutrien
    for nutrient in nutrition_data[food]:
        # Mengambil nama, jumlah, dan satuan nutrien
        name = nutrient
        value = nutrition_data[food][nutrient]
        unit = "g"  #satuan gram
        # Mencetak data nutrisi
        print(f"{name:<20}{value:<10}{unit:<10}")

def thisFood():
    while True:
        food = str(input('Masukan nama makanan: '))
        food = food.lower()
        # Menambahkan pengecekan apakah makanan ada dalam data nutrisi
        if food in nutrition_data:
            print_nutrition(food)
            if food in healthy_foods:
                print(f"{food} adalah makanan sehat.")
            elif food in unhealthy_foods:
                print(f"{food} adalah makanan tidak sehat")
        else:
            print(f"{food} tidak terdaftar dalam data, Anda bisa melakukan pengecekan manual")
        print('Coba lagi [Y/N]? ')
        back = input("Apakah anda ingin cek BMI lagi ? (y/n) ")
        if back == "n":
            print("="*35, "\n")
            print('Program telah berakhir, anda akan kembali ke menu utama')
            time.sleep(4)
            os.system('cls')
            break
        
    