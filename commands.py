from base import *

def run(command: str, state: State) -> int:
    # menerima command yang diberikan dan state program
    # fungsi-fungsi spesifikasi memanipulasi state program lewat side effects
    # nilai return adalah -1 (keluar), 0 (normal), 1 (kesalahan)
    
    if command == "exit":
        return -1
    elif command == "login":
        return login(state)
    elif command == "logout":
        return logout(state)
    # lanjutkan spam elif :v
    else:
        print("Perintah tidak diketahui")
        return 1

def login(state: State) -> int:
    users = state[0]
    
    if state[3][0] != ANON[0]:
        print("Pengguna sudah login!")
        return 1
    
    username = input("Username: ")
    password = input("Password: ")

    i = 0
    while users[i][0] != USER_MARK[0]:
        if username == users[i][0]:
            if password == users[i][1]:
                state[3] = users[i]
                print(f"Selamat datang, {state[3][0]}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return 0
            else:
                print("Password salah")
                return 1
        i += 1
            
    print("Username tidak terdaftar!")
    return 1

def logout(state: State) -> int:
    if state[3][0] == ANON[0]:
        print("Pengguna belum login!")
        return 1
    
    state[3] = ANON
    return 0