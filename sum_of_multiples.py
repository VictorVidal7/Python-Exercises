'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Examples:
solution(10) # 23
solution(20) # 78
solution(-5) # 0'''

def solution(number):
    if number < 0:
        return 0
    else:
        return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])
    
def solution(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0]) if number > 0 else 0
    
print(solution(10)) # 23
print(solution(20)) # 78
print(solution(-5)) # 0