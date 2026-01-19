# solving using the len and short . Len to identifiy if the strings is elligible for being anagram or not , then shorting nad matching 
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

first = input("Enter first word: ")
second= input("Enter second word: ")

if is_anagram(first, second):
    print("Yes, it is an anagram!")
else:
    print("No, it is not an anagram!"
