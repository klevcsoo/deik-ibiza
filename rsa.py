import random

from euklidesz import gcd, extended_gcd
from miller_rabin import is_probable_prime


def generate_prime_number(bits):
    while True:
        n = random.getrandbits(bits)
        if is_probable_prime(n):
            return n


def generate_rsa_keys(bit_length):
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


def encrypt_rsa(msg, pub_key):
    e, n = pub_key
    if msg < 0 or msg >= n:
        raise ValueError("Message is out of range for encryption.")
    return pow(msg, e, n)


def decrypt_rsa(cipher_text, priv_key):
    d, n = priv_key
    if cipher_text < 0 or cipher_text >= n:
        raise ValueError("Ciphertext is out of range for decryption.")
    return pow(cipher_text, d, n)


def validate_rsa_keys(pub_key, priv_key):
    e, n = pub_key
    d, m = priv_key
    return (e * d) % m == 1


# Example usage:

# Generate RSA keys
public_key, private_key = generate_rsa_keys(bit_length=1024)

# Validate RSA keys
valid = validate_rsa_keys(public_key, private_key)
print("RSA keys are valid:", valid)

# Encrypt and decrypt a message
message = 42
ciphertext = encrypt_rsa(message, public_key)
decrypted_message = decrypt_rsa(ciphertext, private_key)

print("Original message:", message)
print("Ciphertext:", ciphertext)
print("Decrypted message:", decrypted_message)
