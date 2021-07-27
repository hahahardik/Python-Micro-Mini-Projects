#Sum of Digits: The Harder Way

def sum_digits(num):

    sum_i = 0

    for i in range(0, len(str(num))):
        rem = (num%(10**(i+1)) - num%(10**(i))) / (10**i)
        sum_i += rem
        
    print(int(sum_i))
