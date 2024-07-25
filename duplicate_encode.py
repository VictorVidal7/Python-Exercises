'''The goal of this exercise is to convert a string to a new string where each character in the new string is "(" 
if that character appears only once in the original string, or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...
It Should encode XXX", the "XXX" is the expected result, not the input!'''

def duplicate_encode(word):
    word = word.lower()
    result = ""
    for w in word:
        if word.count(w) == 1:
            result += '('
        else:
            result += ')'
    return result

def duplicate_encode(word):
    word = word.lower()
    dict_freq = {}
    for w in word:
        if w in dict_freq:
            dict_freq[w] = dict_freq[w] + 1
        else:
            dict_freq[w] = 1
    
    result = ""
    for w in word:
        if dict_freq[w] == 1: 
            result += '('
        else: 
            result += ')'
    return result

def duplicate_encode(word):
    #shortest solution
    return "".join(['(' if word.lower().count(w) == 1 else ')' for w in word.lower()])            