def Palindrome(text):
    if text == text[::-1]:
        return("True")
    else:
        return("False")
 
text = "potop"
print(Palindrome(text))