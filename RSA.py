# algorithm
def secure_prime_generator():
    yield from [
        251352642263889039868309043894037481379002996715589396370854987834622532561522720403074015628816522584866374785754812790090831773387112312703220610291993961566100333483106513061700679351674883108504663868999773335993131871433147375498526830250690800432950741107471775936506033522777378528889986463928680062779,
        234601306906702217804957533486106543816960131695391266497422573355527800260716665381597389816091857137372406177664905766000014102540204528163683625043444669386812465309478832002368041295429725611772236019022712629169757194963880836723186721316763532024657471001347998077008043814690024358601642733925216784203,
]

def modinv(x, y):
    r, s = 1, 0
    while y:
        r, s = s, r -x // y * s
        x, y = y, x % y
    return r

def rsa_generate_keys():
    p, q = secure_prime_generator()
    n = p * q
    t = n - p - q + 1
    e = 65537
    d = modinv(e, t) % t
    assert (d * e) % t == 1
    return (e, n), (d, n)

def rsa(plaintext, public_key):
    return pow(plaintext, *public_key)

# keys
public_key, secret_key = rsa_generate_keys()
public_key
secret_key

# encryption
ciphertext = rsa(0xfacade17, public_key)
ciphertext

plaintext = rsa(ciphertext, secret_key)
hex(plaintext)
