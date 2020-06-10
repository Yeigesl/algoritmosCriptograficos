s=""
def KSA(key):
    keylength = len(key)
    s=list(range(256))
    print ('State inicial\n')
    print(s)
    print('\n')
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % keylength]) % 256
        
        s[i], s[j] = s[j], s[i]  # swap
    print ('State final \n')
    print(s)
    print('\n')
    return s
def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K
def RC4(key):
    S = KSA(key)
    return PRGA(S)
def main():
    key = 'EF CD AB 89 67 54 32 01'
    plaintext = 'Por mi raza hablara el espiritu'
    def convert_key(s):
        return [ord(c) for c in s]
    key = convert_key(key)
    keystream = RC4(key)
  
    print('Texto cifrado:')
    import sys
    for c in plaintext:
        sys.stdout.write("%02X " % (ord(c) ^ next(keystream)))
    print
    print('\n')
main()
