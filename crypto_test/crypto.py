from Crypto.Hash import SHA256
from Crypto.Signature import DSS
from Crypto.PublicKey import DSA


def main():
    message = b"uzenet"
    key = DSA.generate(1024)

    h = SHA256.new(message)
    signer = DSS.new(key, "fips-186-3")
    signature = signer.sign(h)
    print(str(signature))

    pub_key = key.public_key()
    verifier = DSS.new(pub_key, "fips-186-3")
    if verifier.verify(h, signature):
        print("az üzenet autentikus")
    else:
        print("az üzenet NEM autentikus")


if __name__ == "__main__":
    main()
