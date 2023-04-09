# import untuk typing fungsi atau mengunakan konstanta
# DEFINISI TIPE

# Berdasarkan PEP 484 self tidak diberikan type dan return type __init__ adalah None
class User:
    def __init__(self, username: str, password: str, role: str) -> None:
        self.username = username
        self.password = password
        self.role = role
        
class Temple:
    def __init__(self, id: int, creator: str, 
                 sand: int, rock: int, water: int) -> None:
        self.id = id
        self.creator = creator
        self.sand = sand
        self.rock = rock
        self.water = water
        
class Material:
    def __init__(self, name: str, description: str, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity

class State:
    def __init__(self, users: list[User], temples: list[Temple],
                 materials: list[Material], c_user: User) -> None:
        self.users = users
        self.temples = temples
        self.materials = materials
        self.c_user = c_user # current user

# DEFINISI KONSTANTA
MAX_USER = 102 # 100 jin + roro + bondo
MAX_TEMPLE = 100 # lebih dari 100 tidak disimpan

# asumsi username tidak boleh memiliki whitespace sebelum karakter pertama
ANON = User(" ", " ", " ") # pengguna belum login
USER_MARK = User(" MARK", "ZUCKER", "BERG") # mark pengguna berupa seorang alien

TEMPLES_MARK = Temple(-1, "Malin Kundang", 0, 0, 0) # mark candi berupa sebuah gunung

DEFAULT_MATERIALS = [Material("pasir", "pasir pantai Nyi Roro Kidul", 0),
                     Material("batu", "batu dari Mars", 0),
                     Material("air", "Nyi Roro Kidul bath water (air Laut Selatan)", 0)]