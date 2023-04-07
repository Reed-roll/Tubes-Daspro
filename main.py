import load
from commands import run
from base import *

users = load.users # matriks data user
temples = load.temples # matriks data candi
materials = load.materials # data bahan bangunan

current_user = ANON # anggap username " " jika belum login
state = [users, temples, materials, current_user] # state program untuk di-pass ke command yang dijalankan

# main loop
while True:
    command = input(">>> ")
    
    status = run(command, state)
    if status == -1:
        break