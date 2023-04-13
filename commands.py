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
    # lanjutkan spam elif :v
    else:
        print("Perintah tidak diketahui")
        return 1

def save(state: State) -> int:
    if not (state.c_user.role == "bandung_bondowoso"
            or state.c_user.role == "roro_jonggrang"):
        print("Akses command terbatas pada Bandung dan Roro!")
        return 1
    
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
        data.save(state, data.dir)
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