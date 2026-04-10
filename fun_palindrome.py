# def palindrome(x):
#     num = x
#     temp = 0


def is_palindrome(text):
    text = text.lower()           # convert to lowercase
    reversed_text = text[::-1]    # reverse the string
    
    if text == reversed_text:
        return True
    else:
        return False


# Taking input from user
word = input("Enter a word: ")

if is_palindrome(word):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    
    
