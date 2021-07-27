#Rounding of floats to nearest interger
# If it has 0.5 as fraction, add 0.5

import math

# Save the input data into a text file (for large data)
with open('round_off.txt') as f:
    content = f.read()
    #split the data into num (separator = space)
    num = content.split( )
    
div = []

for i in range(0, len(num), 2):
    quo = int(num[i]) / int(num[i+1])

    #math.modf(num) gives the fractional and numerical part in form of a tuple
    #Ex. for math.modf(7.24), it will give (0.24, 7.00)

    #checking if the fraction is 0.5 or not
    if math.modf(quo)[0] == 0.5:
        quo += 0.5
        div.append(quo)
    else:
        div.append(quo)


#Rounding off digits
round_num = [round(i) for i in div]

print(round_num)

