def make_key(key):
    if len(key) != len(set(key)) or len(key) == 0:
        raise ValueError('wrong key.')
    elif(len(key)%2 != 0):
        raise ValueError('wrong key.')
        
    box = {}
    
    for i in range(len(key)):
        if(i%2 == 0):
            box[key[i]] = key[i+1]
        else:
            box[key[i]] = key[i-1]
            
    return box


def make_encryptor(key = 'malinowebuty'):
    new = make_key(key)
    
    def encryptor(txt):
        lst = []
        for i in range(len(txt)):
            lst.append(txt[i])
            for public, secret in new.items():
                if(lst[i] == public):
                    lst[i] = secret
                    break
        word=""
        for elem in lst:
            word += elem
    
        return word
    return encryptor


if __name__ == '__main__':
    txt = input("enter text: ")
    cipher = make_encryptor()
    print("encrypted: ", cipher(txt))
