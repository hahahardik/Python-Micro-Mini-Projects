#Average of array
#Refer to the 'average_of_array.txt' file for the format of data
#Avg of for a single array of intergers is simple though

import math

with open('average_of_array.txt') as f:
    c = f.readlines()

#To split data by space and stored in the form of strings
list_num = []
for line in c:
    list_num.append(line.split( ))

#To store avegare values(floats)
avg = []

for i in list_num:
    sum_i = 0
    for j in range(0, len(i) - 1):
        sum_i += int(i[j])
    sums.append(sum_i)
    avg.append(sum_i / (len(i)-1))

print(avg)
 
#For round them off (optional)   
div = []

for num in avg:
    #math.modf(num) gives the fractional and numerical part in form of a tuple
    #Ex. for math.modf(7.24), it will give (0.24, 7.00)

    #checking if the fraction is 0.5 or not
    if math.modf(num)[0] == 0.5:
        num += 0.5
        div.append(num)
    else:
        div.append(num)


#Rounding off digits
round_num = [round(i) for i in div]

#final rounded-off list
print(round_num)
