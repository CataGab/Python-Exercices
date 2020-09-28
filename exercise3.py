"""
exercise3.py
vowel count
created by sands 1/11/10
"""

def vowels(s) :
    """
    counts vowels in string
    argument: s: str
    returns: number of vowels in s: int
    """
    result = 0
    n = 0
    while n<len(s):
        if s[n] in "AEIOUaeiou" : result = result+1
        n = n+1
    return result

line = input("Type a line of text: ")
print("The line contains", vowels(line), "vowels")

