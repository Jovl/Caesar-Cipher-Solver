import sys

encrypted = sys.argv[1]
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decrypt(n, ciphertext):
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]

        except ValueError:
            result += l

    return result


def show_result(plaintext, n):
    decrypted = decrypt(n, encrypted)

    print('Shift: %s' % (26 - n))
    print('Cipher Text: %s' % plaintext)
    print('Decrypted Text: %s\n' % decrypted)


for x in range(1, 27):
    show_result(encrypted, x)
