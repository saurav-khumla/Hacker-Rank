a=int(input());
b=0;
c=1;
d=0;
for i in range(0,a,1):
    print(b); # 0   1      1
    d=b+c;    #0+1  1+1   1+2
    b=c;     # 1    1     2
    c=d;    # 1   2       3

