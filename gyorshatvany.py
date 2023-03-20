def gyorshatvany(alap: float, exp: float, mod: int):
    alap %= mod

    if exp == 0:
        return 0
    elif exp == 1:
        return alap
    elif exp % 2 == 0:
        return gyorshatvany(alap * alap % mod, exp / 2, mod)

    return alap * gyorshatvany(alap, exp - 1, mod) % mod
