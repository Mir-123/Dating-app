#!usr/local/bin/python3.8
# -*- coding: utf-8 -*import
from _collections import deque
 
# Creating the male stack and female queue
matches = 0
males = deque(map(int, input().split()))
females = deque(map(int, input().split()))
 
# Cycling until any of the 2 deque(s) becomes empty
while males and females:
    male = males[-1]
    female = females[0]
 
    # Check if anyone is equal or below 0
    if male <= 0 or female <= 0:
        if male <= 0:
            males.pop()
        if female <= 0:
            females.popleft()
        continue
 
    # Check when both are above 0
    elif male > 0 and female > 0:
        if male % 25 == 0 or female % 25 == 0:
            if male % 25 == 0:
                if len(males) > 1:
                    males.pop()
                    males.pop()
                else:
                    males.pop()
            if female % 25 == 0:
                if len(females) > 1:
                    females.popleft()
                    females.popleft()
                else:
                    females.popleft()
            continue
        if male == female:
            matches += 1
            males.pop()
            females.popleft()
        else:
            del females[0]
            males[-1] -= 2
 
 
print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join(map(str, males))}')
else:
    print('Males left: none')
if females:
    print(f'Females left: {", ".join(map(str, females))}')
else:
    print('Females left: none')
