def cCipher(str1, shift = 2):
    if (type(str1) == str):
        # print('loc 1')
        str2 = []
        str3 = []
        for i in range(0,len(str1)):
            # print('loc 2')
            # str2[i] = ord('str1[i]') + shift
            x = str1[i]
            # str2.append(ord(str(x)))
            str3.append(ord(str1[i]) + shift)
        
        mystr = ''
        for i in str3:
            mystr = mystr + chr(i)
        return mystr
    else:
        print('the input is not a string')
        return 0


print(cCipher('i love you',3))

