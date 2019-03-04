import random

def parser(input_txt_file):
    '''
    Takes a .txt file and returns ALL printable characters as LIST
    '''
    with open(input_txt_file,'r') as ff:
        a = ff.read()
        b = a.replace('\n','').replace(' ','')
    res = []
    for elem in b:
        res.append(elem)
        # print(type(a))
    return res

def main():
    original = parser('test.txt')
    k = 3
    rot_alphabet = []
    for i in alphabet:
        rot_alphabet.append(chr((ord(i) - ord('a') + 3) % 26 + ord('a')))

    ciphertext = []
    for i in original:
        ciphertext.append(rot_alphabet[ord(i) - ord('a')])
        print(i)
    print(original)
    print(ciphertext)

if __name__ == '__main__':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    main()
