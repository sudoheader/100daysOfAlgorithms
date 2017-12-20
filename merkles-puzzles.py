from os import urandom
from hashlib import sha1
from random import shuffle, choice
# algorithm
puzzle_size = 2 ** 16
def merkles_puzzle():
    secrets = [None] * puzzle_size
    puzzles = [None] * puzzle_size

    for i in range(puzzle_size):
        # generate secret
        secrets[i] = urandom(16)

        # pair := secret|index
        pair = secrets[i] + int.to_bytes(i, 4, 'big')
        # plaintext := pair|sha1(pair)
        plaintext = pair + sha1(pair).digest()

        # cipthertext := ENCRYPT(plaintext, key)
        key = urandom(10)
        noise = sha1(key).digest()
        noise += sha1(noise).digest()
        ciphertext = bytes(i ^ j for i, j in zip(plaintext, noise))

        # puzzle := ciphertext|key
        puzzles[i] = ciphertext + key[2:]

    # randomize order
    shuffle(puzzles)

    # return
    return secrets, puzzles

def solve_puzzle(puzzle):
    ciphertext = puzzle[:40]
    key = puzzle[40:]

    for i in range(puzzle_size):
        # guess key
        noise = sha1(int.to_bytes(i, 2, 'big') + key).digest()
        noise += sha1(noise).digest()

        # plaintext := DECRYPT(ciphertext, key)
        plaintext = bytes(i ^ j for i, j in zip(ciphertext, noise))

        # pair|digest := key|index|sha1(pair)
        pair = plaintext[:20]
        digest = plaintext[20:]

        # on match: time, key, index
        if sha1(pair).digest() == digest:
            return i, pair[:16], int.from_bytes(pair[16:], 'big')

# (I) alice
alice_secrets, public_puzzles = merkles_puzzle()

# (II) bob
bob_time, bob_secret, public_index = solve_puzzle(choice(public_puzzles))

print('Bob has secret and publishes index')
print('key:', bob_secret)
print('index:', public_index)
print('steps executed:', bob_time)

# (III) alice
print('Alice has secret')
print('key:', alice_secrets[public_index])

# (IV) adversary
total_time, total_puzzles = 0, 0

for puzzle in public_puzzles:
    adv_time, adv_key, adv_index = solve_puzzle(puzzle)
    total_time += adv_time
    total_puzzles += 1

    if adv_index == public_index:
        print('very unlikely! adversary found secret:', adv_key)
        break

    if total_time > bob_time * 100:
        print('adversary failed to find secret')
        break

print('searched puzzles:', total_puzzles, 'steps executed:', total_time)
