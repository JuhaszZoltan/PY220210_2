import lotto_fgs as f

lotto_tipus = f.sorslas_tipus_beker()

if lotto_tipus == -1:
    print('viszlát :/')
else:
    tippek = f.tippeket_beker(lotto_tipus)
    print(f'a szelvényeden a köv. számok vannak beXelve: {tippek}')
    nyeroszamok = f.nyeroszam_generalas(lotto_tipus)
    print('a sorsolás megtörtént')
    print(f'a nyerőszámok: {nyeroszamok}')
    talalatok = f.talalatok_szama(tippek, nyeroszamok)
    print(f'összesen {talalatok} találatod volt')
    if talalatok > 0: print('grat!')