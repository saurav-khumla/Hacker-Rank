spam=int(input())
if spam==1:
    print('Hello')
    for i in range(1,11):
        print(i)
elif spam==2:
    print('Howdy')
    i=1
    while (i<11):
        print(i)
        i=i+1
else:
    print("Greetings!")
