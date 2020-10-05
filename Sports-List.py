

sports = ["basketball", "softball", "football", "baseball", "track"]  


f = open("Sports-List.txt", "w+")

for i in sports:
    f.write(i+'\n') 
    f.close