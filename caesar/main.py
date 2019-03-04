import random

def parser(input_txt_file):
    '''
    Takes a .txt file and returns ALL printable characters as STRING
    '''
    with open(input_txt_file,'r') as ff:
        a = ff.read()
        blacklist = [',','.','?','!','(',')',';','’','"','--','-',' ','\n','\t']
    for item in blacklist:
        a = a.replace(item,'')
    res = a.lower()
    return res


def caesar_ciph(text,steps,ciph = True,alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    '''
    Input: A string.
    OUTPUT: A ciphered (deciphered) string
    '''
    # k = 3
    n = len(alphabet)
    if not(ciph):
         steps = -steps
    ciph_alphabet = {}
    for i,char in enumerate(alphabet):
        ciph_alphabet[char] = alphabet[(i + steps)%n] # (chr((ord(i) - ord('a') + steps) % 26 + ord('a')))
    ciphertext = []
    for char in text:
        # print(ord(i) - ord('a'))
        ciphertext.append(ciph_alphabet[char])
        
    # print(text)
    res = ''.join(ciphertext)
    print(res)
    return res

def main():
    original = parser('test.txt')
    ciphered = caesar_ciph(original,3,ciph = True)
    print('---------------------------')
    caesar_ciph(ciphered,3,ciph = False)

if __name__ == '__main__':
    main()
