import data
from commands import run
from base import *

t_user = data.t_user # tabel data user
t_temple = data.t_temple # tabel data candi
t_material = data.t_material # tabel bahan bangunan

c_user = ANON # current user, anggap username " " jika belum login
state = State(t_user, t_temple, t_material, c_user) # state program untuk di-pass ke command yang dijalankan

# main loop
while True:
    command = input(">>> ")
    
    status = run(command, state)