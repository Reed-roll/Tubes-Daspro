import data
from base import *
import random
from util import hitungJumlah

def run(command: str, state: State) -> int:
    # menerima command yang diberikan dan state program
    # fungsi-fungsi spesifikasi memanipulasi state program lewat side effects
    # nilai return adalah 0 (normal), 1 (kesalahan)
    
    if command == "exit":
        exit(state)
        return 1 # kalau berhasil return, exit gagal
    elif command == "login":
        return login(state)
    elif command == "logout":
        return logout(state)
    elif command == "save":
        return save(state)
    elif command == "summonjin":
        return summonjin(state)
    elif command == "hapusjin":
        return hapusjin(state)
    elif command == "ubahjin":
        return ubahjin(state)
    elif command == "cekUser":
        return cekUser(state)
    elif command == "bangun":
        return bangun(state)
    elif command == "kumpul" :
        return kumpul(state)
    elif command == "batchkumpul":
        return batchkumpul(state)
    elif command == "batchbangun":
        return batchbangun(state)
    elif command == "cekBahan":
        return cekBahan(state)
    elif command == "cekCandi":
        return cekCandi(state)
    # lanjutkan spam elif 
    else:
        print("Perintah tidak diketahui")
        return 1

def save(state: State) -> int:
    dir = input("Masukkan nama folder: ")
    return data.save(state, dir)
    
def exit(state: State) -> None:
    while True:
        choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if choice == "Y" or choice == "y":
            to_save = True
            break
        elif choice == "N" or choice == "n":
            to_save = False
            break
    
    if to_save:
        data.save(state, "")
        quit()
    else:
        quit()

def login(state: State) -> int:
    users = state.t_user.users
    n = state.t_user.length
    
    if state.c_user.username != ANON.username:
        print("Pengguna sudah login!")
        return 1
    
    username = input("Username: ")
    password = input("Password: ")

    # contoh loop setelah penggunaan tabel
    for i in range(n):
        if (users[i].username != USER_MARK.username
        and username == users[i].username):
            if password == users[i].password:
                state.c_user = users[i]
                print(f"Selamat datang, {state.c_user.username}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return 0
            else:
                print("Password salah")
                return 1
    
    print("Username tidak terdaftar!")                
    return 1

def logout(state: State) -> int:
    if state.c_user.username == ANON.username:
        print("Pengguna belum login!")
        return 1
    
    state.c_user = ANON
    return 0

def bangun(state : State) :
    if(state.c_user != "Bondowoso") and (state.c_user != "Roro") and state.c_user != ANON and state.c_user.role == "Pembangun":
        pasir = random.randint(1,5)
        batu = random.randint(1,5)
        air = random.randint(1,5)
        
        if pasir <= state.t_material.materials[0].quantity and batu <= state.t_material.materials[1].quantity and air <= state.t_material.materials[2].quantity:
            print("Candi berhasil di bangun.")
            idx = 0
            if(state.t_temple.length < 100):
                for d in range(1,state.t_temple.length + 1):
                    ada = False
                    for i in range(state.t_temple.length):
                        if(d == state.t_temple.temples[i].id):
                            ada = True
                            break
                    
                    if not ada :
                        idx = d
                        break
                    else:
                        idx = d + 1
                    
                if(idx == 0):
                    idx = 1
                
                if(state.t_temple.temples[state.t_temple.length].id == -1) and state.t_temple.length <= 99 :
                    state.t_temple.temples[state.t_temple.length] = Temple(idx, state.c_user.username,pasir,batu,air)
                    state.t_temple.length += 1

            print("Sisa candi yang perlu di bangun : ",100-state.t_temple.length,".")
            for k in range(3):
                if(state.t_material.materials[k].name == "pasir"):
                    state.t_material.materials[k].quantity -= pasir
                elif(state.t_material.materials[k].name == "batu"):
                    state.t_material.materials[k].quantity -= batu
                elif(state.t_material.materials[k].name == "air"):
                    state.t_material.materials[k].quantity -= air
            return 0
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
            return 1
    else: 
        print("Cuman jin pembangun yang bisa membangun candi")
        return 1

def kumpul(state : State) :
    if(state.c_user != "Bondowoso") and (state.c_user != "Roro") and state.c_user != ANON and state.c_user.role == "Pengumpul":
        pasir = random.randint(0,5)
        batu = random.randint(0,5)
        air = random.randint(0,5)

        print("Jin menemukan ",pasir," pasir ", batu , " batu, dan ", air , " air.")
        for k in range(3):
            if(state.t_material.materials[k].name == "pasir"):
                state.t_material.materials[k].quantity += pasir
            elif(state.t_material.materials[k].name == "batu"):
                state.t_material.materials[k].quantity += batu                
            elif(state.t_material.materials[k].name == "air"):
                state.t_material.materials[k].quantity += air
    else:
        print("Cuman jin pengumpul yang bisa melakukan kumpul.")
    
def batchkumpul(state : State):
    if(state.c_user.username == "Bondowoso"):
        i = 0
        jumlah_pengumpul = 0
        pasir = 0
        batu = 0
        air = 0

        while state.t_user.users[i].role != USER_MARK.role and i < MAX_USER:
            if(state.t_user.users[i].role == "Pengumpul"):
                jumlah_pengumpul += 1
                pasir += random.randint(0,5)
                batu += random.randint(0,5)
                air += random.randint(0,5)
            i += 1
        if(jumlah_pengumpul == 0):
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else:
            print("Mengerahkan ", jumlah_pengumpul, " jin untuk mengumpulkan bahan.")
            print("Jin menemukan total ", pasir, " pasir, ", batu, " batu, dan ", air, " air.")
            for k in range(3):
                if(state.t_material.materials[k].name == "pasir"):
                    state.t_material.materials[k].quantity += pasir
                elif(state.t_material.materials[k].name == "batu"):
                    state.t_material.materials[k].quantity += batu
                elif(state.t_material.materials[k].name == "air"):
                    state.t_material.materials[k].quantity += air

    else: 
        print("Cuman Bondowoso yang bisa melakukan batchkumpul.")

def batchbangun(state : State):
    if(state.c_user.username == "Bondowoso"):
        i = 0
        jumlah_pembangun = 0
        pasir = 0
        batu = 0
        air = 0
        TBahan = [-1,-1,-1,-1]
        bahan = [TBahan for i in range(100)]
        while state.t_user.users[i].role != USER_MARK.role and i < MAX_USER:
            if(state.t_user.users[i].role == "Pembangun") :
                pasir = random.randint(1,5)
                batu = random.randint(1,5)
                air = random.randint(1,5)
                bahan[jumlah_pembangun] = [pasir,batu,air,state.t_user.users[i].username]
                jumlah_pembangun += 1
            i += 1
        
        TotPasir = hitungJumlah(bahan,0,jumlah_pembangun-1)
        TotBatu = hitungJumlah(bahan,1,jumlah_pembangun-1)
        TotAir = hitungJumlah(bahan,2,jumlah_pembangun-1)

        if(jumlah_pembangun == 0):
            print("Kumpul gagal.Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        elif TotPasir <= state.t_material.materials[0].quantity and TotBatu <= state.t_material.materials[1].quantity and TotAir <= state.t_material.materials[2].quantity:   
            print("Mengerahkan ", jumlah_pembangun, " jin untuk membangun candi dengan total bahan ", TotPasir, " pasir, " , TotBatu, " batu, dan ",TotAir, " air." )    
            print("Jin berhasil membangun total ", jumlah_pembangun, " candi.") 
            j = 0
            idx = 0
            while j < jumlah_pembangun and state.t_temple.length < 100:
                for d in range(1,state.t_temple.length + 1):
                    ada = False
                    for i in range(state.t_temple.length):
                        if(d == state.t_temple.temples[i].id):
                            ada = True
                            break
                    
                    if not(ada) :
                        idx = d
                        break
                    else:
                        idx = d + 1
                if (idx == 0):
                    idx = 1
                if state.t_temple.temples[state.t_temple.length].id == -1 and state.t_temple.length < 100:
                    state.t_temple.temples[state.t_temple.length] = Temple(idx, bahan[j][3],bahan[j][0],bahan[j][1],bahan[j][2])
                    j += 1
                    state.t_temple.length += 1
            for k in range(3):
                if(state.t_material.materials[k].name == "pasir"):
                    state.t_material.materials[k].quantity -= pasir
                elif(state.t_material.materials[k].name == "batu"):
                    state.t_material.materials[k].quantity -= batu
                elif(state.t_material.materials[k].name == "air"):
                    state.t_material.materials[k].quantity -= air
        else:
            print("Mengerahkan ", jumlah_pembangun, " jin untuk membangun candi dengan total bahan ", TotPasir, " pasir, " , TotBatu, " batu, dan ",TotAir, " air." )  
            kurang_pasir = TotPasir - state.t_material.materials[0].quantity if(TotPasir > state.t_material.materials[0].quantity) else 0
            kurang_batu =  TotBatu - state.t_material.materials[1].quantity if(TotBatu > state.t_material.materials[0].quantity) else 0
            kurang_air = TotAir - state.t_material.materials[2].quantity if(TotAir > state.t_material.materials[0].quantity) else 0
            print("Bangun gagal. Kurang ",kurang_pasir, " pasir, " , kurang_batu, " batu, dan " , kurang_air ," air.")
            

def cekBahan(state : State):
    print(state.t_material.materials[0].quantity)
    print(state.t_material.materials[1].quantity)
    print(state.t_material.materials[2].quantity)

def cekCandi(state : State):
    print(state.t_temple.temples[0].id , " " ,state.t_temple.temples[0].creator )
    print(state.t_temple.temples[1].id, " " ,state.t_temple.temples[1].creator)
    print(state.t_temple.temples[2].id, " " ,state.t_temple.temples[2].creator)
    print(state.t_temple.temples[3].id, " " ,state.t_temple.temples[3].creator)
    print(state.t_temple.temples[4].id, " " ,state.t_temple.temples[4].creator)

def cekUser (state : State):
    for i in range(state.t_user.length):
        print(state.t_user.users[i].username," " ,state.t_user.users[i].role)
    

def summonjin(state: State):
    if state.c_user.username != "Bondowoso":
        print("Hanya Bondowoso yang bisa melakukan summon jin.")
        return 1
    elif state.t_user.length >= MAX_USER:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        return 1
    else:
        n = state.t_user.length
        indekskosong = 0

        # for i in range(n):
        #     if state.t_user.users[i].username == USER_MARK.username:
        #         indekskosong = i
        #         break
        i = 0
        while state.t_user.users[i].username != USER_MARK.username:
            i += 1
            if state.t_user.users[i].username == USER_MARK.username:
                indekskosong = i
                break
            elif i > MAX_USER:
                print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
                return 1

        # print("indeks kosong adalah",indekskosong)
        print("Jenis jin yang dapat dipanggil:")
        print("   (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("   (2) Pembangun - Bertugas membangun candi")

        jenisjin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

        if (jenisjin < 0 or jenisjin > 2): #salah input
            print(f'Tidak ada jenis jin bernomor "{jenisjin}"! ')
            return 1

        elif jenisjin == 1:
            tipejin = "Pengumpul"
            print(f'Memilih jin "Pengumpul".')

        else: # jenisjin == 2
            tipejin = "Pembangun"
            print(f'Memilih jin "Pembangun".')
            
        loop1 = True
        while loop1 == True:
            usernamejin = input("Masukkan username jin: ")
            loop2 = False
            sudahdiambil = False

            for f in range(MAX_USER):
                if state.t_user.users[f].username == usernamejin:
                    sudahdiambil = True

            if sudahdiambil == True:
                print(f'Username "{usernamejin}" sudah diambil!')
            else:
                # state.t_user.users[indekskosong].username = usernamejin
                # print(f'username jin berhasil menjadi "{state.t_user.users[indekskosong].username}"')
                loop2 = True

            while loop2 == True:
                passwordjin = input("Masukkan password jin: ")

                if len(passwordjin) < 5 or len(passwordjin) > 25:
                    print("Password panjangnya harus 5-25 karakter!")
                else:
                    # state.t_user.users[indekskosong].password = passwordjin
                    print(f'password jin berhasil menjadi "{state.t_user.users[indekskosong].password}"')
                    loop2 = False
                    loop1 = False

        state.t_user.users[indekskosong] = User(usernamejin, passwordjin, tipejin)
        state.t_user.length += 1
        
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print()
        print(f'jin "{usernamejin}" berhasil dipanggil!')
        
def hapusjin(state: State):
    if state.c_user.username == "Bondowoso":
        
        usernamejin = input("Masukkan username jin: ")

        #cari indeks jin, jika tidak ada return false
        indeksjin = 0
        while state.t_user.users[indeksjin].username != usernamejin: #user dengan username jin
            if indeksjin > state.t_user.length:
                print(f'Tidak ada jin dengan username tersebut.')
                return 1
            indeksjin += 1 
            
        choice = input(f"Apakah Anda yakin ingin menghapus jin dengan username {usernamejin} (Y/N)? ")
        
        if choice == "y" or choice =="Y":
            
            #hilangkan jin
            state.t_user.users[indeksjin] = USER_MARK
            
            #menghilangkan candi
            indekscandi = 0
            jumlahcandihilang = 0
            
            while indekscandi < MAX_TEMPLE:
                if state.t_temple.temples[indekscandi].creator == usernamejin:
                    state.t_temple.temples[indekscandi] = TEMPLE_MARK
                    state.t_temple.length -= 1
                indekscandi += 1
            print("Jin telah berhasil dihapus dari alam gaib.")
            return 0
        
        elif choice == "n" or choice =="N":
            return 0
        
        else:
            print("Input salah, silahkan ulangi lagi.")
            return 1
    else:
        print("Hanya Bondowoso yang bisa mengakses hapusjin")
        return 1

def ubahjin(state: State):
    if state.c_user.username == "Bondowoso":
        usernamejin = input("Masukkan username jin: ")
        
        indeksjin = 0
        while state.t_user.users[indeksjin].username != usernamejin: #user dengan username jin
            if indeksjin > MAX_USER:
                print(f'Tidak ada jin dengan username tersebut.')
                return 1
            indeksjin += 1 

        tipejin = state.t_user.users[indeksjin].role

        if tipejin == "Pembangun":
            tipejinbaru = "Pengumpul"
        elif tipejin == "Pengumpul":
            tipejinbaru = "Pembangun"
        else:
            print("User tersebut bukan jin.")
            return 1

        choice = input(f'Jin ini bertipe "{tipejin}". Yakin ingin mengubah ke tipe "{tipejinbaru}"(Y/N)? ')

        if choice == "y" or choice == "Y":
            state.t_user.users[indeksjin].role = tipejinbaru
            print("Jin telah berhasil diubah.")
        elif choice == "n" or choic == "N":
            return 0
        else:
            print("Input salah, silahkan ulangi lagi.")
            return 1
    
    else:
        print("Hanya Bondowoso yang bisa mengakses ubahjin.")
        return 1