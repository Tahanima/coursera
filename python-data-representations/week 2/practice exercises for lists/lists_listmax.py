"""
Template - Compute the largest number in a list
"""

def list_max(numbers):
    """
    Given a list of numbers, return the maximum (largest) number
    in the list
    """
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
            
    return max_num

# Tests
print(list_max([4]))
print(list_max([-3, 4]))
print(list_max([5, 3, 1, 7, -3, -4]))
print(list_max([1, 2, 3, 4, 5]))


# Output
#4
#4
#7
#5