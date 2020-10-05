# Function used to sum up numbers in a list

def c(a):
    b = 0
    for i in a:
        b += i
    return b


print(c([4, 5, 2, -3]))
