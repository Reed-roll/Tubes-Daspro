from base import *
from util import split_n
import argparse
import os

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

# pengen dijadiin prosedur tapi tipe list inputnya beda-beda ...
# data pengguna - list[ list[str, str, str] ]
with open(os.path.join(folder_path, "user.csv")) as f:
    f.readline()
    i = 0
    for line in f:
        users[i] = split_n(line, 3, ";")
        i += 1
        
# data candi - list[ list[int, str, int, int, int] ]
with open(os.path.join(folder_path, "candi.csv")) as f:
    f.readline()
    i = 0
    for line in f:
        temp = split_n(line, 5, ";")
        temples[i] = [int(temp[0]), temp[1], int(temp[2]), int(temp[3]), int(temp[4])]
        i += 1

# data bahan-bahan - list[ list[str, str, int] ]
with open(os.path.join(folder_path, "bahan_bangunan.csv")) as f:
    f.readline()
    i = 0
    for line in f:
        temp = split_n(line, 3, ";")
        materials[i] = [temp[0], temp[1], int(temp[2])]
        i += 1
        
print("Selamat datang di program \"Manajerial Candi\"")
print("Silahkan masukkan username Anda")