'''You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. 
You may assume the argument is non-negative.

Examples:(Input --> Output)
1 --> 4
2 --> -1
7 --> -1
10 --> -1
345 --> -1
3456 --> 3600
9 --> 16
25 --> 36
144 --> 169
'''

def find_next_square(sq):
    if (sq**0.5).is_integer():
        return (int(sq**0.5)+1)**2
    else:
        return -1

def find_next_square(sq):
    return (int(sq**0.5)+1)**2 if (sq**0.5).is_integer() else -1