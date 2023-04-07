def split_n(s: str, n: int, sep: str) -> list[str]:
    # memisahkan s menjadi n bagian
    # s adalah string yang akan dipecah
    # n adalah jumlah pecahan
    # sep adalah separator atau karakter pemisah
    i = 0
    j = 0
    res = ["" for i in range(n)]
    
    while s[j] != "\n":
        if s[j] == sep:
            i += 1
        else:
            res[i] += s[j]
        j += 1
    
    return res