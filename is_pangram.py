'''A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

Example: (Input --> Output)
"The quick brown fox jumps over the lazy dog." --> True
"This is not a pangram." --> False
'''
import string
def is_pangram(st):
    for i in string.ascii_lowercase:
        if i not in st.lower():
            return False
    return True

def is_pangram(st):
    return [True if all(i in st.lower() for i in string.ascii_lowercase) else False][0]

def is_pangram(st):
    return set(string.ascii_lowercase) <= set(st.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog.")) # True
print(is_pangram("This is not a pangram.")) # False