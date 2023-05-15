from euklidesz import extended_gcd
from gyorshatvany import gyorshatvany
from miller_rabin import is_probable_prime
from rsa import generate_rsa_keys, encrypt_rsa_text, decrypt_rsa_text, sign_text, verify_signature_text

if __name__ == "__main__":
    print("kibővített euklideszi algoritmus")
    for (a, b) in [(211, 45), (2340, 113), (1491, 23)]:
        (d, x, y) = extended_gcd(a, b)
        print(f"{d} = {a}*{x} + {b}*{y}")

    print("\ngyorshatványozás")
    for (alap, exp, mod) in [(9, 22, 79), (129, 97, 171), (23, 209, 211)]:
        result = gyorshatvany(alap, exp, mod)
        print(f"{alap}^{exp} ≡ {result} (mod {mod})")

    print("\nmiller-rabin prímteszt")
    print(is_probable_prime(561))

    print("\nrsa (szöveg)")
    message = input("kérek egy üzenetet: ")
    public_key, private_key = generate_rsa_keys(bit_length=1024)
    print(f"publikus kulcs (e, n): {public_key}")
    print(f"privát kulcs (d, n): {private_key}")

    signature = sign_text(message, private_key)
    print(f"aláírás: {signature}")

    ciphertext = encrypt_rsa_text(message, public_key)
    print(f"titkosított üzenet: {ciphertext}")
    decrypted_message = decrypt_rsa_text(ciphertext, private_key)
    print(f"feloldott üzenet: {decrypted_message}")

    if verify_signature_text(decrypted_message, signature, public_key):
        print("aláírás egyezik, üzenet hiteles")
    else:
        print("aláírás nem egyezik, üzenet NEM hiteles")
