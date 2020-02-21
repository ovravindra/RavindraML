'''
def testcase(letters):
    x = len(letters)
    a = letters[x-1].lower()
    b = letters[x-2].lower()
    print(a+' '+b)

letters = 'baT'
print(testcase(letters))
'''

def balanced_parens(line):
    x = str(line)
    y = ''
    count = 0
    for i in x:
        if i == '(':
            count += 1
            y += '('
        elif i == ")":
            count -= 1
            y += ')'
    
    if count == 0:
        z = ('Y'+' '+y)
    else:
        z = ('N'+' '+y)
    
    return z

line = '((1+2)*(3-4))'
print(balanced_parens(line))
