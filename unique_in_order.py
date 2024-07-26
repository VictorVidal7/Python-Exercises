'''Implement the function unique_in_order which takes as argument a sequence and returns a list of items without 
any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]'''

def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    else:
        new = []
        for i in range(len(sequence)):
            if (i+1) < len(sequence):
                if sequence[i] != sequence[i+1]:
                    new.append(sequence[i])
            else:
                new.append(sequence[i])
        return new

def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    else:
        unique = [sequence[0]]
        for i in range(1, len(sequence)):
            if sequence[i] != sequence[i-1]:
                unique.append(sequence[i])
        return unique
    
def unique_in_order(sequence):
    return [sequence[i] for i in range(len(sequence)) if i == 0 or sequence[i] != sequence[i-1]]
    
print(unique_in_order('AAAABBBCCDAABBB')) # ['A', 'B', 'C', 'D', 'A', 'B'
print(unique_in_order('ABBCcAD')) # ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1, 2, 2, 3, 3])) # [1, 2, 3]