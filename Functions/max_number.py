# def max_element(lst):
#     return max(lst)

# lst = [20 , 30,6,7,990]
# print(max_element(lst))


# second option
def find_max(lst):
    max_value = lst[0]

    for num in lst:
        if num > max_value:
            max_value = num
    

    return max_value


numbers = [7,9,6,5,8]
print("Maximum element is " ,find_max(numbers))

