def isPalindrome(s: str) -> bool:
    s = ''.join(c for c in s if c.isalnum()).lower()
    return True if s==s[::-1] else False

print(isPalindrome("A man, a plan, a canal: Panama"))