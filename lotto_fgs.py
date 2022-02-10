import random

def felso_hatar(lotto_tipus):
    max = -1
    if   lotto_tipus == 5: max = 90
    elif lotto_tipus == 6: max = 45
    elif lotto_tipus == 7: max = 35
    return max


def tippeket_beker(tippek_szama):
    max_tipp = felso_hatar(tippek_szama)
    tippek = []
    sorszam = 1
    while len(tippek) < tippek_szama:
        tipp = int(input(f'mi a {sorszam}. tipped?: '))
        if tipp not in tippek and tipp <= max_tipp and tipp > 0:
            tippek.append(tipp)
            sorszam += 1
        else:
            print('ez a tipp nem megfelelő')
    tippek.sort()
    return tippek


def sorslas_tipus_beker():
    tipus = int(input('Melyik játéktípust választja? [5, 6 vagy 7]: '))
    if tipus in [5, 6, 7]:
        return tipus
    else:
        print('bocs, ilyen lotto nincs :(')
        return -1


def nyeroszam_generalas(nyeroszamok_szama):
    max = felso_hatar(nyeroszamok_szama)
    nyeroszamok = []
    while len(nyeroszamok) < nyeroszamok_szama:
        szam = random.randint(1, max)
        if szam not in nyeroszamok:
            nyeroszamok.append(szam)
    nyeroszamok.sort()
    return nyeroszamok


def talalatok_szama(tipp_lista, nyero_lista):
    talalat = 0
    for t in tipp_lista:
        if t in nyero_lista:
            talalat += 1
    return talalat