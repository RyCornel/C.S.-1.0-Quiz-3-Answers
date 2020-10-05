def get_file_lines():
    filename = open("sports.txt", "r")
    content_list = filename.readlines()
    for i in content_list:
        print(i)
    filename.close()
    
get_file_lines()