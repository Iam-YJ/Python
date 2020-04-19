#jeju_coding_part7(61~70)

#61

#62
string = "abbcccddddddddd"

a = string.count("g") #0
b= string.count("a") #1
c=string.count("b") #2
d=string.count("d") #9
e = string.count("c")

print(str(c)+str(a)+str(b)+str(d)+str(a)+str(d)+str(c)+str(e))

#63
data = list(map(str,input("문장 입력: ")))
simple1=[]
simple2=[]

data.append(" ")

for i in range(len(data)):
    simple1.append(data[i])

    if data[i] == ' ':
        simple2.append(simple1[0])
        simple1.clear()
        
for s in simple2:
    print(s, end='')
print()


#64

#65
a=[1,2,3,4]
b=[a,b,c,d]

c=['a','b','c','d']

for i in range(4):
    b[i]=c[i]

print("[",end='')
for i in range(4):
    print(f"[{a[i]}",end='')
    print(f",{b[i]}]",end='')
print("]")

#66
top= ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
rule="ABD"
topl=[]

rulel=list(rule)
print(rulel)


#67 답확인 안
def solution(n):    
    l=[]
    for i in range(20):
        l.append((i*(i-3))//2)

    for i in range(len(l)):
        if n>l[i] and n<l[i+1]:
            time=l[i] #실제횟수
            people=i #참가자
            min = n-time-1 #민규
            
    print(f"[{min},{people}]")
    

#68

bus = ["12:30", "13:20", "14:13"]
time = "12:40"

buss=[]
bw=[]
r = []

g="'지나갔습니다'"
h=0
m=0

times = time.split(":")
th = int(times[0])
tm = int(times[1])
tw = th*60 + tm

for i in range(len(bus)):
    buss.append(bus[i].split(":"))

for i in range(3):
    bw.append((int(buss[i][0])*60 + int(buss[i][1]))-tw)

print("[",end='')
for i in range(3):
    if int(bw[i]) < 0:
        print(g,end=', ')
    else:
        if int(bw[i]) > 0 and int(bw[i])<60:
            m = int(bw[i])
            print(f"'0시간 {m}분'",end=', ')
        else:
            h = int(bw[i]) // 60
            m = int(bw[i]) - 60
            print(f"'{h}시간 {m}분'",end='')
print("]",end='')
print()

#69


#70
a = ([1, 2],
     [2, 4])
b = ([1, 0],
     [0, 3])

c=[]

if (len(a[1])) == (len(b[0])):
    for i in range(2):
        d=[]
    for j in range(2):
        d.append((int(a[i][0]) * int(b[0][j])) + (int(a[i][1]) * int(b[1][j])))
        c.append(d)
    print(c)
else:
    print(-1)


    

        




