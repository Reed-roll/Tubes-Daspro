# DEFINISI TIPE
User = list[str, str, str] # (username, password, role)
Temple = list[int, str, int, int, int] # (id, pembuat, pasir, batu, air)
Material = list[str, str, int] # (nama, deskripsi bebas, jumlah)

State = list[list[User], list[Temple], list[Material], User]

# DEFINISI KONSTANTA
MAX_USER = 102 # 100 jin + roro + bondo
MAX_TEMPLE = 100 # lebih dari 100 tidak disimpan
MAX_MATERIALS = 3 # pasir, batu, air

# asumsi username tidak boleh memiliki whitespace sebelum karakter pertama
ANON = [" ", " ", " "] # pengguna belum login
USER_MARK = [" MARK", "ZUCKER", "BERG"] # mark pengguna berupa seorang alien
TEMPLES_MARK = [-1, "Malin Kundang", "0", "0", "0"] # mark candi berupa sebuah gunung