# Caesar Cipher is crypting a message by shifting the letters

def cCipher(str1, shift = 2):
    if (type(str1) == str):
        
        str3 = [] 
        for i in range(0,len(str1)):

            str3.append(ord(str1[i]) + shift)
        
        mystr = '' # starting an empty string

        for i in str3:
            mystr = mystr + chr(i) # converting the ascii numbers into characters and concatinating them
        return mystr
    else:
        print('the input is not a string')
        return 0


print(cCipher('i love you', 3))

