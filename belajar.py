import re
handle = open('mbox-short.txt')
count = 0
for line in handle:
    line = line.rsplit()
    if re.search('From:', line):
        count += 1
        print(line)
        
print("Count: ",count)