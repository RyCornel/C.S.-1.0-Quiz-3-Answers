#Q4 Code Quality

# Function used to sum up integers in a list

def sum_the_list(integer_list):
    
    sum = 0
    
    for i in integer_list:
        sum += i
    return sum


print(sum_the_list([4, 5, 2, -3]))
