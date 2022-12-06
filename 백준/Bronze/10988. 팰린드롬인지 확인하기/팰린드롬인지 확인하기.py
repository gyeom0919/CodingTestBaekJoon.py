n = input()

def palindrome(word):
    i = 0
    while i < len(n):
        for a in n:
            i += 1
            if a == n[-i]:
                continue
            else:
                return 0
        return 1
    
print(palindrome(n))