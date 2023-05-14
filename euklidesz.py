def gcd(a: int, b: int):
    """
    Euklideszi algoritmus (legnagyobb közös többszörös)
    """
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int):
    """
    Kibővített euklideszi algoritmus
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd_val, x, y = extended_gcd(b % a, a)
        return gcd_val, y - (b // a) * x, x
