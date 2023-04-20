from base import *
import util
import argparse
import os

def copy(state: State) -> State:
    t_user = TabUser([User(state.t_user.users[i].username,
                    state.t_user.users[i].password,
                    state.t_user.users[i].role) 
                    for i in range(MAX_USER)],
                    state.t_user.length)

    t_temple = TabTemple([Temple(state.t_temple.temples[i].id,
                        state.t_temple.temples[i].creator,
                        state.t_temple.temples[i].sand,
                        state.t_temple.temples[i].rock,
                        state.t_temple.temples[i].water) 
                        for i in range(MAX_TEMPLE)],
                        state.t_temple.length)

    t_mat = TabMaterial([Material(state.t_material.materials[i].name,
                        state.t_material.materials[i].description,
                        state.t_material.materials[i].quantity) 
                        for i in range(MATERIALS_COUNT)],
                        state.t_material.length)
    
    # undo tidak akan me-logout bondo
    return State(t_user, t_temple, t_mat, state.c_user)

def snap(state: State, history: History) -> History:
    stack = [BASE_STATE for i in range(history.length + 1)]
    for i in range(1, history.length + 1):
        stack[i] = history.stack[i - 1]
    stack[0] = state
    
    return History(stack, history.length + 1)

def get_arr(file: str, max: int) -> list[list[str]]:
    res = [["__EOP__"] for i in range(max)]
    
    with open(os.path.join(dir, file)) as f:
        f.readline()
        i = 0
        for line in f:
            res[i] = util.split(line, ";")
            i += 1
    return res

def write(filename: str, los: list[str], mark: str, length: int, header: str) -> None:
    text = header + "\n"
    for i in range(length):
        if los[i] != mark:
            text = text + los[i] + "\n"

    with open(filename, "w") as f:
        f.write(text)

def save(state: State, dir: str) -> int:
    # low level saving for F14 and F16
    # TODO: Menyimpan state dalam file
    print("Saving ...")

    users = [util.merge_n([state.t_user.users[i].username,
                        state.t_user.users[i].password,
                        state.t_user.users[i].role], 3, ";")
             for i in range(state.t_user.length)]
    
    u_mark = USER_MARK.username + ";" + USER_MARK.password + ";" + USER_MARK.role
    
    temples = [util.merge_n([str(state.t_temple.temples[i].id),
                        state.t_temple.temples[i].creator,
                        str(state.t_temple.temples[i].sand),
                        str(state.t_temple.temples[i].rock),
                        str(state.t_temple.temples[i].water)], 5, ";")
               for i in range(state.t_temple.length)]
    
    t_mark = (str(TEMPLE_MARK.id) + ";" + TEMPLE_MARK.creator + ";" +
            str(TEMPLE_MARK.sand) + ";" + str(TEMPLE_MARK.rock) + ";" +
            str(TEMPLE_MARK.water))

    materials = [util.merge_n([state.t_material.materials[i].name,
                            state.t_material.materials[i].description,
                            str(state.t_material.materials[i].quantity)], 3, ";")
                 for i in range(state.t_material.length)]
    
    dir = "save/" + dir
    dir_count = util.count_sep(dir, "/")
    dir_names = util.split(dir, "/")

    path = os.path.join(root)

    for i in range(dir_count):
        path = os.path.join(path, dir_names[i])
        if not os.path.isdir(path):
            print(f"Membuat folder {path} ...")
            os.mkdir(path)
        
    write(os.path.join(path, "user.csv"),
          users, u_mark, state.t_user.length,
          "username;password;role")
    
    write(os.path.join(path, "candi.csv"),
          temples, t_mark, state.t_temple.length,
          "id;pembuat;pasir;batu;air")
          
    write(os.path.join(path, "bahan_bangunan.csv"),
          materials, "", state.t_material.length,
          "nama;deskripsi;jumlah")
    
    return 0

# ambil path program yang dijalankan
root = os.path.dirname(os.path.realpath(__file__))

# ambil argumen folder yang akan dibaca datanya
parser = argparse.ArgumentParser()
parser.add_argument('folder', help="nama folder yang berisi data program",
                    nargs='?' ,default="")

# cek apakah argumen folder yanag diberi valid
args = parser.parse_args()
if args.folder == "":
    print("Tidak ada nama folder yang diberikan!\n")
    print("Usage: python main.py <nama_folder>")
    quit()
    
dir = os.path.join(root, args.folder)
if not os.path.isdir(dir):
    print(f"Folder {dir} tidak ditemukan.")
    quit()

# mulai baca data
print("Loading...")

# tabel pengguna
t_user = TabUser([USER_MARK for i in range(MAX_USER)], 0)

# tabel candi
t_temple = TabTemple([TEMPLE_MARK for i in range(MAX_TEMPLE)], 0) 

# tabel bahan-bahan bangunan
t_material  = TabMaterial(DEFAULT_MATERIALS, MATERIALS_COUNT)

# data pengguna
temp_users = get_arr("user.csv", MAX_USER)
for i in range(MAX_USER):
    if temp_users[i][0] != "__EOP__":
        t_user.users[i] = User(temp_users[i][0], temp_users[i][1], temp_users[i][2])
        t_user.length += 1

# data candi
temp_temples = get_arr("candi.csv", MAX_TEMPLE)
for i in range(MAX_TEMPLE):
    if temp_temples[i][0] != "__EOP__":
        t_temple.temples[i] = Temple(int(temp_temples[i][0]), temp_temples[i][1],
                            int(temp_temples[i][2]), int(temp_temples[i][3]), int(temp_temples[i][4]))
        t_temple.length += 1

# data bahan-bahan
temp_mats = get_arr("bahan_bangunan.csv", MATERIALS_COUNT)
for i in range(MATERIALS_COUNT):
    name = temp_mats[i][0]
    for j in range(MATERIALS_COUNT):
        if t_material.materials[j].name == name:
            t_material.materials[j] = Material(temp_mats[i][0], 
                                        temp_mats[i][1], int(temp_mats[i][2]))
    
print("Selamat datang di program \"Manajerial Candi\"")
print("Silahkan masukkan username Anda")