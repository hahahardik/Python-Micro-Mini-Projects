#Modulo Operator

# File contains list of operations to be performed on the first digit
#Ex. 5 + 3 * 7 + 10 * 2 * 3 + 1 % 11
#The second last bing the modulo operator and last one being the divisor


def mod_op('file'):

    with open('modulo_operator.txt') as f:
        c = f.read().split( )

    print(c)

    #Data is stored as strings in list c

    num = int(c[0])

    for i in range(1, len(c), 2):
        if c[i] == '+':
            num += int(c[i+1])
        elif c[i] == '*':
            num *= int(c[i+1])
        elif c[i] == '-':
            num -= int(c[i+1])
        elif c[i] == '/':
            num /= int(c[i+1])
        else:
            continue
    
    #final = result after modulo       
    final = num % int(c[len(c)-1])

    print(final)

