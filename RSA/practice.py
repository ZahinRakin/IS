from math import gcd


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def key_generator() -> tuple:
    while True:
        p = int(input('Enter a prime number: '))
        q = int(input('Enter another prime number: '))

        if not is_prime(p) or not is_prime(q):
            print('Both numbers must be prime. Please try again.')
        else:
            break

    n, phi = p * q, (p - 1) * (q - 1)
    e = d = 2
    while gcd(e, phi) != 1:
        e += 1
    while (d * e) % phi != 1:
        d += 1
    return (n, e), (n, d)


def encrypt(message: str, key) -> list:
    n, e = key
    encrypted = [(pow(ord(char), e, n)) for char in message]
    return encrypted


def decrypt(encrypted: list, key) -> str:
    n, d = key
    decrypted = [chr(pow(val, d, n)) for val in encrypted]
    return ''.join(decrypted)


if __name__ == '__main__':
    private_key, public_key = key_generator()
    print(private_key, public_key)
    encrypted_message = encrypt('hello world!', public_key)
    print(encrypted_message)
    decrypted_message = decrypt(encrypted_message, private_key)
    print(decrypted_message)
