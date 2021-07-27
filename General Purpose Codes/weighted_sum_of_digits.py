#Weighted Sum of Digits
# Starting from left
#Ex. for 4563, it will be 4*1 + 5*2 + 6*3 + 3*4

def sum_digits(num):

    sum_i = 0

    for i in range(0, len(str(num))):
        rem = (num%(10**(i+1)) - num%(10**(i))) / (10**i)
        sum_i += (rem*(len(str(num)) - i))
        
    print(int(sum_i))
        
