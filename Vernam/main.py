import random
test_string = 'tonnikolhtonphraneseenakaravimoutsokai'
alphabet = 'abcdefghijklmopqrstuvwxyz'

def keygen(test_string):
    '''
    Creates the Key, given the message
    '''
    n = len(test_string)
    # test = []
    # for i in range(n):
    test = random.choices(test_string,k=n)
    return (''.join(test))
def cipher(test_string,key):
    '''
    Ciphering the given string
    '''
    to_bytes = [ord(elem) for elem in test_string]
    key_b = [ord(elem) for elem in key]
    ciph_text = [chr(elem[0] ^ elem[1]) for elem in zip(key_b,to_bytes)]
    return (''.join(ciph_text))
# def de_cipher(test_string,key):
#     '''
#     Deciphering the given string
#     '''
#     to_bytes = [ord(elem) for elem in test_string]
#     key_b = [ord(elem) for elem in key]
#     ciph_text = [chr(elem[0] ^ elem[1]) for elem in zip(key_b,to_bytes)]
#     print(''.join(ciph_text))
key = keygen(test_string)
ciphered = cipher(test_string,key)
print(cipher(test_string,key))
print('--------------------------------------------------')
print(cipher(ciphered,key))
