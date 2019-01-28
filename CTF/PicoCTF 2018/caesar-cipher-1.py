def decipher(cipher_string, key):
    # Caesar Cipher is a substitution cipher, which works by shifting letters.
    # The shift is decided by a key, which is supplied by the user
    decipher_string = ""
    for i in cipher_string:
        decipher_letter = ord(i) - key
        if decipher_letter < 97:
            # This is the wrap-around code for deciphering the cipher text
            # First we calculate the displacement from the 'A'
            # Which can directly be used as displacement from 'Z'. Adding +1 to it gives us the letter
            decipher_letter = ord('z') - (ord('a') - decipher_letter) + 1
        decipher_string += chr(decipher_letter)
    return decipher_string


if __name__ == '__main__':
    for i in range(1, 26):
        print(f"For key {i} Decipher {decipher('yjhipvddsdasrpthpgrxewtgdqnjytto', i)}")
