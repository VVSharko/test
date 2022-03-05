import string

"""I wrote two sample finctions. The string module is optional"""

def isPalindrome(s):
    if not isinstance(s, str):
        raise TypeError
    s = s.translate({ord(c): None for c in string.whitespace})
    s = s.lower()
    rev = s[::-1]
    if s == rev:
        return True
    return False
    
def isPalindrome2(s):
    if not isinstance(s, str):
        raise TypeError
    s = s.translate({ord(c): None for c in string.whitespace})
    s = s.lower()
    length = len(s)
    for i in range(0, length//2):
        if s[i] != s[length - i - 1]:
            return False
    return True
