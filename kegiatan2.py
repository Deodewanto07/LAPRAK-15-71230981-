import re  

txt = "Sang mata-mata sedang memata-matai kasus kaca mata di toko Matahari"
x = re.search("\s", txt)
y = re.search("saya", txt)


if x:
    print("Spasi ditemukan di:", x.start())
else:
    print("Spasi tidak ditemukan.")

if y:
    print("Kata 'saya' ditemukan.")
else:
    print("Kata 'saya' tidak ditemukan.")
    
import re  
handle = open('mbox-short.txt')

for line in handle:
    line = line.rstrip()  
    if re.search('^X-.*: [0-9.]+', line):
        print(line)  
