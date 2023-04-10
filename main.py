import data
from commands import run
from base import *

users = data.users # matriks data user
temples = data.temples # matriks data candi
materials = data.materials # data bahan bangunan

c_user = ANON # current user, anggap username " " jika belum login
state = State(users, temples, materials, c_user) # state program untuk di-pass ke command yang dijalankan

# main loop
while True:
    command = input(">>> ")
    
    status = run(command, state)