def check_palindrome(list):
    number=[]
    for i in list:
        if str(i)==str(i)[::-1]:
            number.append(i)
    return number

list=[121, 345, 111, 234]
result = check_palindrome(list)
print("palindrome no =" ,result)