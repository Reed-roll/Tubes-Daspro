from base import *
import util
import argparse
import os

def get_arr(file: str, max: int) -> list[list[str]]:
    res = [["__EOF__"] for i in range(max)]
    
    with open(os.path.join(dir, file)) as f:
        f.readline()
        i = 0
        for line in f:
            res[i] = util.split(line, ";")
            i += 1
            
    return res


def save(state: State, dir: str) -> int:
    # low level saving for F14 and F16
    # TODO: Menyimpan state dalam file
    print("Saving ...")
    dir_count = util.count_sep(dir, "/")
    dir_names = util.split(dir, "/")

    path = root
    for i in range(dir_count):
        path = os.path.join(path, dir_names[i])
        if not os.path.isdir(path):
            print(f"Membuat folder {path} ...")
            os.mkdir(path)
    return 0

root = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('folder', help="nama folder yang berisi data program",
                    nargs='?' ,default="")

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

# array pengguna
users = [USER_MARK for i in range(MAX_USER)]

# array candi
temples = [TEMPLE_MARK for i in range(MAX_TEMPLE)] 

# array bahan-bahan bangunan
materials  = DEFAULT_MATERIALS

# data pengguna
t_users = get_arr("user.csv", MAX_USER)
i = 0
while t_users[i][0] != "__EOF__":
    users[i] = User(t_users[i][0], t_users[i][1], t_users[i][2])
    i += 1
        
# data candi
t_temples = get_arr("candi.csv", MAX_TEMPLE)
i = 0
while t_temples[i][0] != "__EOF__":
    temples[i] = Temple(int(t_temples[i][0]), t_temples[i][1],
                        int(t_temples[i][2]), int(t_temples[i][3]), int(t_temples[i][4]))
    i += 1

# data bahan-bahan

t_materials = get_arr("bahan_bangunan.csv", MAX_TEMPLE)
i = 0
while t_materials[i][0] != "__EOF__":
    materials[i] = Material(t_materials[i][0], t_materials[i][1], int(t_materials[i][2]))
    i += 1

print("Selamat datang di program \"Manajerial Candi\"")
print("Silahkan masukkan username Anda")