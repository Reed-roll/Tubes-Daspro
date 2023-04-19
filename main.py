import data
from commands import run
from base import *
import copy

t_user = data.t_user # tabel data user
t_temple = data.t_temple # tabel data candi
t_material = data.t_material # tabel bahan bangunan

c_user = ANON # current user, anggap username " " jika belum login
state = State(t_user, t_temple, t_material, c_user) # state program untuk di-pass ke command yang dijalankan

situation = [copy.deepcopy(state)]
# main loop
while True:
   
    command = input(">>> ")
    if(command == "undo"):
        situation = data.delete(situation)
        state = copy.deepcopy(situation[data.length(situation)-1])
    else:
        status = run(command, state)
        if(status != -99):
            situation = data.append(situation,copy.deepcopy(state))
        
