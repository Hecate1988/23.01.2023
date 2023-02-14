def is_palindrome(s: str):
    import string
    for i in range(0, len(string.punctuation)):
        s = s.replace(string.punctuation[i], '')
    s = s.split(' ')
    for i in range(0, len(s)):
        s[i] = s[i].lower()
    string = ''.join(s)
    return string[::-1] == string

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("0P"))
print(is_palindrome("a."))

assert is_palindrome("A man, a plan, a canal: Panama") == True, 'Test1'
assert is_palindrome("0P") == False, 'Test2'
assert is_palindrome("a.") == True, 'Test3'
print("ОК")