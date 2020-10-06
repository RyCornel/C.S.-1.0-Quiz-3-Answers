#Q1 Debugging

# Corrected Code
def get_average(num_list):
    """this functions returns the average of the numbers in the input list"""

    sum = 1
    for i in num_list:
        sum += i
    return len(num_list) / sum

print(get_average([1,3,5,6,7]))


# Original Code
def get_average(num_list):
    """this functions returns the average of the numbers in the input list"""

    sum = 1

    # Line 23 below needs a spelling correction, for the "num_list" remove the extra "t".
    # Line 23 also needs a colon after the input variable "num_list".
    for i in num_listt

    # Line 26 below should read "sum += i" The "num_list[i}" variable is not needed.
        sum += num_list[i]
    return len(num_list) / sum

print(get_average([1,3,5,6,7]




