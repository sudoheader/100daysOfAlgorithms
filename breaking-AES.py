from Crypto import Random
from Crypto.Cipher import AES

# AES-CBC
def encrypt(plaintext):
    # initialize AES
    random = Random.new()
    iv = random.read(16)
    key = random.read(16)
    aes = AES.new(key, AES.MODE_CBC, iv)

    # add PKCS#7 padding
    pad = 16 - len(plaintext) % 16
    plaintext += bytes([pad] * pad)

    # encrypt
    ciphertext = iv + aes.encrypt(plaintext)

    return key, ciphertext

def decrypt(ciphertext, key):
    # initialize AES
    iv = ciphertext[:16]
    aes = AES.new(key, AES.MODE_CBC, iv)

    # decrypt
    plaintext = aes.decrypt(ciphertext[16:])

    # check PKCS#7 padding
    pad = plaintext[-1]
    if pad not in range(1, 17):
        raise Exception()
    if plaintext[-pad:] != bytes([pad] * pad):
        raise Exception()

    # remove padding
    return plaintext[:-pad]

# secure service
def secure_service(message):
    secret_key = b'\xed\xcc\xb5\x8a\xf4\x8f\xd9\x1e\x1bS\xce~p\xa2s\xcc'

    # decrypt message
    plaintext = decrypt(message, secret_key)

    # process message
    try:
        from json import loads
        print('ACK', loads(plaintext))
    except Exception:
        raise ValueError()

# adversarial client
def attack(message):
    reconstructed = b''

    while len(message) >= 32:
        # retrieved block
        block = [0] * 16

        # byte in block
        for i in range(1, 17):
            # PKCS#7 padding
            pad = [0] * (16 - i) + [i] * i

            for x in range(256):
                # tested byte
                block[-i] = x
                if x == i:
                    continue

                # alter message
                test = bytearray(message)
                for j in range(16):
                    test[-32 + j] ^= block[j] ^ pad[j]
                test = bytes(test)

                try:
                    # call service
                    secure_service(test)
                except ValueError as e:
                    break  # incorrect content
                except Exception as e:
                    pass   # incorrect padding
            else:
                block[-i] = i

        # store retrieved block and continue
        reconstructed = bytes(block) + reconstructed
        message = message[:-16]

    return reconstructed

intercepted_message = b'\xd97\xea\xc8\xfe\xdf\x06\xf7b3\x16UG\xd5#>\xa8\x1c.l\xf1+\xc9H\xbd\xb1\x91\x90\xc0\xac?\x92\x1c\xa0\x08\xc7d/\x10\xe6\xae\xe0 F\x1a\x13\xc1\xb0\xf0,\xd7\xb9\xca\xfb\xde\x13\xa5\xfd92\xff*\x17\xbc\x8f\xd3Z\xe81\x8f\x1c\xb4\x17@\xeb5\t\xa4\x16\xb2\x07\x06\xd6\x83x\xac\xf3\xc9\xb2\xb7\xf6Q3\xc0\x7f\x92\xd4p\xfeV\xad{\xc7(}\x8f[L>\x08\xab\xfe'

attack(intercepted_message)
