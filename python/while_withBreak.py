# while loop with break
while True:
    print('please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you')


# while loop with continue

while True:
    print('what is your age')
    age = int(input())
    if age > 23:
        continue
    print('age is '+str(age))
    break
print('end')


