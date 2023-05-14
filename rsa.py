import random

from euklidesz import gcd, extended_gcd
from miller_rabin import is_probable_prime


def generate_prime_number(bits):
    while True:
        n = random.getrandbits(bits)
        if is_probable_prime(n):
            return n


def generate_rsa_keys(bit_length: int):
    p = generate_prime_number(bit_length // 2)
    q = generate_prime_number(bit_length // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    if d < 0:
        d += phi

    return (e, n), (d, n)


def encrypt_rsa(value: int, public_key: tuple[int, int]):
    e, n = public_key
    if value < 0 or value >= n:
        raise ValueError("Túl nagy szám a titkosításhoz.")
    return pow(value, e, n)


def encrypt_rsa_text(text: str, public_key: tuple[int, int]):
    char_values = [ord(c) for c in text]
    return [encrypt_rsa(c, public_key) for c in char_values]


def decrypt_rsa(cipher_value: int, private_key: tuple[int, int]):
    d, n = private_key
    if cipher_value < 0 or cipher_value >= n:
        raise ValueError("Túl nagy szám a visszafejtéshez.")
    return pow(cipher_value, d, n)


def decrypt_rsa_text(ciphertext: list[int], private_key: tuple[int, int]):
    char_array = [chr(c) for c in [decrypt_rsa(c, private_key) for c in ciphertext]]
    return "".join(char_array)


def validate_rsa_keys(public_key: tuple[int, int], private_key: tuple[int, int]):
    e, n = public_key
    d, m = private_key
    return (e * d) % m == 1
