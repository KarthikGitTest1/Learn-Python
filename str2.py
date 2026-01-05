
# s = "Python"
# rev = ""
# for ch in s:
#     rev = ch + rev
#     print(rev)

# print(rev)
# s = "Python"
# rev1 = "".join(reversed(s))

# print(rev1)
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]


# print(reverse_string("Python"))
# import re
# text = "I Love Python"
# rev = " ".join(word[::-1] for word in text.split())
# print(rev)
# s = "madam"
# is_palindrome = s.lower() == s[::-1].lower()
# print(is_palindrome)


# def is_palindrome(s1):
#     s1 = re.sub(r'[^a-zA-Z0-9]', '', s1).lower()
#     return s1 == s1[::-1]


# print(is_palindrome("A man, a plan, a canal: Panama"))

# s = "I love Python programming"
# words = s.split()
# longest = max(words, key=len)
# print(longest)
def is_pal(n):

    rev = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    print(rev)


is_pal(12345)

s = "I love Python"
result = " ".join(word[::-1] for word in s.split())
print(result)

duplicates = {ch for ch in s if s.count(ch) > 1}
print(duplicates)
print((duplicates))
