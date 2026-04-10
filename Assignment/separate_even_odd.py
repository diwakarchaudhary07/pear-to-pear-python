def separate_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd


data = [1, 2, 3, 4, 5]
even_list, odd_list = separate_even_odd(data)

print("Even:", even_list)
print("Odd:", odd_list)












