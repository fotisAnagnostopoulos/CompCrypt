# import os
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
a = parser('test.txt')
print(a)