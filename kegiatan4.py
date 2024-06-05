import re  

txt = "Sang mata-mata sedang memata-matai kasus kaca mata di toko Matahari"
x = re.sub("\s", "-", txt)
print(x)  
y = re.sub("\s", "*", txt, 2)
print(y)  