from gyorshatvany import gyorshatvany
from euklidesz import kibovitett_euklideszi_lnko
from miller_rabin import is_prime

if __name__ == "__main__":
    print("kibővített euklideszi algoritmus")
    for (a, b) in [(211, 45), (2340, 113), (1491, 23)]:
        (d, x, y) = kibovitett_euklideszi_lnko(a, b)
        print(f"{d} = {a}*{x} + {b}*{-y}")

    print("\ngyorshatványozás")
    for (alap, exp, mod) in [(9, 22, 79), (129, 97, 171), (23, 209, 211)]:
        result = gyorshatvany(alap, exp, mod)
        print(f"{alap}^{exp} ≡ {result} (mod {mod})")

    print("\nmiller-rabin prímteszt")
    print(is_prime(561))
