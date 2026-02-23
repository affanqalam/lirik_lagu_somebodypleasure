# Import modul 'sys' dan 'time'
import sys
import time

def jalanin_lirik():
    """
    Fungsi untuk menampilkan lirik lagu "Somebody's Pleasure"
    dengan efek ketikan per karakter dan jeda antar baris.
    """
    lirik = [
        "Soul try to figure it out",
        "From where I've been escapin",
        "Running to end all the sin",
        "Get away from the pressure",
        "Wondering to get a love that is so pure",
        "Gotta have to always make sure",
        "That I'm not just somebody's pleasure",
    ]

    # Jeda waktu dalam detik untuk setiap baris
    delay = [1.3, 1.8, 1, 1, 4.5, 0.8, 1]
    # Jeda waktu dalam detik untuk setiap karakter
    delay_karakter = 0.09
    
    print("\n== Somebody Pleasure - Aziz Hedra ==")
    time.sleep(3)

    for i, baris_lagu in enumerate(lirik):
        try:
            # Loop untuk menampilkan setiap karakter dengan jeda
            for char in baris_lagu:
                print(char, end='')
                sys.stdout.flush() # Memastikan output langsung dicetak
                time.sleep(delay_karakter) 
            
            # Menambahkan jeda setelah setiap baris lirik
            time.sleep(delay[i])
            print('') # Baris baru setelah jeda
        except IndexError:
            # Penanganan error jika list 'delay' tidak sepanjang list 'lirik'
            print("\nError: Daftar jeda (delay) tidak sesuai dengan jumlah baris lirik.")
            break
            
    print("// Code by Affan Qalam Maulana")

# Memanggil fungsi
if __name__ == "__main__":
    jalanin_lirik()
