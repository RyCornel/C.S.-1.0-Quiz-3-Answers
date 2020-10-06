#Q2 File I/O

# Part 1. 
f = open("Sports-List.txt", "w")

sports = ["basketball", "softball", "football", "baseball", "track"]  

f = open("Sports-List.txt", "w+")

for i in sports:
    f.write(i+'\n') 
    f.close

# Part 2.
def get_file_lines():
    filename = open("Sports-List.txt", "r")
    content_list = filename.readlines()
    for i in content_list:
        print(i)
    filename.close()
    
get_file_lines