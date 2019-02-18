import random
def magic8(selectedNumber):
    if selectedNumber==1:
        return 'one '
    elif selectedNumber==2:
        return 'second'
    elif selectedNumber ==3:
        return 'third'
    elif selectedNumber==4:
        return 'fourth'
    elif selectedNumber == 5:
        return 'fifth'
    elif selectedNumber == 6:
        return 'sixth'
    elif selectedNumber == 7:
        return 'seven'
    elif selectedNumber == 8:
        return 'eight'
'''a=random.randint(1,8)      # first way to call function
b=magic8(a)
print(b)'''
print(magic8(random.randint(1,8)))   # second way 
