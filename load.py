from base import *
from util import split_n
import argparse
import os

def get_arr(file: str, n: int, max: int) -> list[list[str]]:
    res = [["__EOF__" for i in range(n)] for j in range(max)]
    
    with open(os.path.join(folder_path, file)) as f:
        f.readline()
        i = 0
        for line in f:
            res[i] = split_n(line, n, ";")
            i += 1
            
    return res

root = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('folder', help="nama folder yang berisi data program",
                    nargs='?' ,default="")

args = parser.parse_args()
if args.folder == "":
    print("Tidak ada nama folder yang diberikan!\n")
    print("Usage: python main.py <nama_folder>")
    quit()
    
folder_path = os.path.join(root, args.folder)
if not os.path.isdir(folder_path):
    print(f"Folder {folder_path} tidak ditemukan.")
    quit()

# mulai baca data
print("Loading...")

# array pengguna
users = [USER_MARK for i in range(MAX_USER)]

# array candi
temples = [TEMPLES_MARK for i in range(MAX_TEMPLE)] 

# array bahan-bahan bangunan
materials  = DEFAULT_MATERIALS

# data pengguna
t_users = get_arr("user.csv", 3, MAX_USER)
i = 0
while t_users[i][0] != "__EOF__":
    users[i] = User(t_users[i][0], t_users[i][1], t_users[i][2])
    i += 1
        
# data candi
t_temples = get_arr("candi.csv", 5, MAX_TEMPLE)
i = 0
while t_temples[i][0] != "__EOF__":
    temples[i] = Temple(int(t_temples[i][0]), t_temples[i][1],
                        int(t_temples[i][2]), int(t_temples[i][3]), int(t_temples[i][4]))
    i += 1

# data bahan-bahan

t_materials = get_arr("bahan_bangunan.csv", 5, MAX_TEMPLE)
i = 0
while t_materials[i][0] != "__EOF__":
    materials[i] = Material(t_materials[i][0], t_materials[i][1], int(t_materials[i][2]))
    i += 1

print("Selamat datang di program \"Manajerial Candi\"")
print("Silahkan masukkan username Anda")