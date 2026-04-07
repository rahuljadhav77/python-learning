# Day 97: Palindrome Test
def is_palindrome(s):
    clean = ''.join(e for e in s if e.isalnum()).lower()
    return clean == clean[::-1]

word = 'Racecar'
print(f'{word} is palindrome: {is_palindrome(word)}')
