# berisi fungsi2 utility untuk pemrosesan data secara general

def count_sep(s: str, sep: str) -> int:
    # menghitung banyak string yang dipisahkan oleh separator
    count = 1
    for i in range(len(s)):
        if s[i] == sep:
            count += 1
    return count

def split(s: str, sep: str) -> list[str]:
    # memisahkan s menjadi n bagian
    # s adalah string yang akan dipecah
    # sep adalah separator atau karakter pemisah
    item_count = count_sep(s, sep)
        
    i = 0
    res = ["" for i in range(item_count)]
    for j in range(len(s)):
        if s[j] == sep:
            i += 1
        elif s[j] != "\n":
            res[i] += s[j]
    
    return res

def merge_n(los: list[str], n: int, sep: str) -> str:
    # menggabungkan suatu list of string menjadi
    # satu string dipisahkan dengan separator
    res = los[0]
    for i in range(1, n):
        res = res + sep + los[i]
    return res

def  hitungJumlah(data : list,index : int,n : int):
    jumlah = 0
    for i in range(n):
        jumlah += data[i][index]

    return jumlah


    