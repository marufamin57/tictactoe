
s1=input('player 1 symbol')
s2=input('player 2 symbol')
def st():
    global b1,q,m
    b1=[' ']*9
    m=1
    q=0
def des():
    global d
    d=input('do you want to play again')

def bo(b):
    for i in range(9):
        if i==0:
            print(b[i],'|',b[i+1],'|',b[i+2])
            print('- '*5)
        if i==3:
            print(b[i],'|',b[i+1],'|',b[i+2])
            print('- '*5)
        if i==6:
            print(b[i],'|',b[i+1],'|',b[i+2])

def win(b):
    global q
    if b[0]==b[1]==b[2]==s1 or b[3]==b[4]==b[5]==s1 or b[6]==b[7]==b[8]==s1:
        q=2
    if b[0]==b[1]==b[2]==s2 or b[3]==b[4]==b[5]==s2 or b[6]==b[7]==b[8]==s2:
        q=1
    if b[0]==b[3]==b[6]==s1 or b[1]==b[4]==b[7]==s1 or b[2]==b[5]==b[8]==s1:
        q=2
    if b[0]==b[3]==b[6]==s2 or b[1]==b[4]==b[7]==s2 or b[2]==b[5]==b[8]==s2:
        q=1
    if b[0]==b[4]==b[8]==s1 or b[2]==b[4]==b[6]==s1:
        q=2
    if b[0]==b[4]==b[8]==s2 or b[2]==b[4]==b[6]==s2:
        q=1

st()

while True:
    if m%2==1:
        print('player 1')
    else:
        print('player 2')
    n=int(input('position'))
    if n<=0 or n>=10:
        print('enter between 1 to 9')
        continue
    if b1[n-1]!=' ':
        print('this is used')
        continue
    for i in range(9):
        if i==(n-1):
            if m%2==1:
                b1[i]=s1
            if m%2==0:
                b1[i]=s2
    bo(b1)
    win(b1)
    if q==2:
        print('winner', s1)
        des()
        if d=='y':
            st()
            continue
        if d=='n':
            break
    if q==1:
        print('winner', s2)
        des()
        if d=='y':
            st()
            continue
        if d=='n':
            break
    m=m+1
    if m==10:
        print('no winner')
        des()
        if d=='y':
            st()
            continue
        if d=='n':
            break
# exec(open('C:\\Users\\maruf\\Desktop\\python\\pyton1\\a1\\a.py').read())