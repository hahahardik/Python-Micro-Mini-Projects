#Vowel Counter

#For large data files
with open('vowel_count.txt') as f:
    c = f.readlines() # .read() statements breaks the line into words and here we want to calculate the vowels in a line.

#for storing no. of vowels in each line
count = []

for line in c:
    vowels = 0
    
    #checking each letter
    for i in range(0, len(line)):
        if line[i] == 'a':
            vowels += 1
        elif line[i] == 'e':
            vowels += 1
        elif line[i] == 'i':
            vowels += 1
        elif line[i] == 'o':
            vowels += 1
        elif line[i] == 'u':
            vowels += 1
        else:
            continue
        
    count.append(vowels)
    
print(count)
