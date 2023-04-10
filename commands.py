import data
from base import *

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
    users = state.users
    
    if state.c_user.username != ANON.username:
        print("Pengguna sudah login!")
        return 1
    
    username = input("Username: ")
    password = input("Password: ")

    i = 0
    while users[i].username != USER_MARK.username:
        if username == users[i].username:
            if password == users[i].password:
                state.c_user = users[i]
                print(f"Selamat datang, {state.c_user.username}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return 0
            else:
                print("Password salah")
                return 1
        i += 1
            
    print("Username tidak terdaftar!")
    return 1

def logout(state: State) -> int:
    if state.c_user.username == ANON.username:
        print("Pengguna belum login!")
        return 1
    
    state.c_user = ANON
    return 0