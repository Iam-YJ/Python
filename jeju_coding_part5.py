#jeju_coding_part5(41~50)
import time

#41
#에라토스테네스의 체

#42
def solution():
    days = 0
    rdays = 0
    
    a = int(input("월 입력:"))
    b = int(input("일 입력:"))

    month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    day = [1,2,3,4,5,6,0]
    
    
    if a>=1 and a<=12:
        for i in range(a):
            days+=month[i]
        rdays = days+b
        print(days)


    if b>=1 and b<=31:
        if rdays % 7 == 1:
            print("WED")
        elif rdays%7==2:
            print("THU")
        elif rdays%7 == 3:
            print("FRI")
        elif rdays%7 == 4:
            print("SAT")
        elif rdays%7 == 5:
            print("SUN")
        elif rdays%7 == 6:
            print("MON")
        elif rdays%7 == 0:
            print("TUE")

#import datetime
#m = int(input())
#d = int(input())
#def findDay(a,b):
#    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
#    return day[datetime.date(2020,a,b).weekday()]
#print(findDay(m,d))


#43
data = int(input("수 입력:"))
bin = []

while data:
    p = data//2
    bin.append(str(data%2))
    data//=2

bin.reverse()
print(bin)
print(''.join(bin))


#44
n = list(map(int,input("숫자 입력 : ")))

sum = 0

for i in range(len(n)):
    sum += n[i]
print(sum)

#45
time_sec = time.time()

year = time_sec//60//60//24//365
print(1970+year)


#46

#47
people = [
             ('이호준', '01050442903'),
             ('이호상', '01051442904'),
             ('이준호', '01050342904'),
             ('이호준', '01050442903'),
             ('이준', '01050412904'),
             ('이호', '01050443904'),
             ('이호준', '01050442903'),
             ]


stu = []
for i in range(len(people)):
    stu.append(people[i][1])

set2 = set(stu)
print(len(set2))


#48
data = list(map(str,input("문자 입력:")))
result=[]

for i in range(len(data)):
    if str(data[i]) >='a' and str(data[i])<='z':
        result.append(data[i].upper())
    elif str(data[i]) >='A' and str(data[i])<='Z':
        result.append(data[i].lower())

for i in range(len(data)):
    print(result[i],end = ' ' )
print()


#49
data = list(map(int,input("숫자 입력:").split()))
print(sorted(data)[-1])

#50

tmp = 0
def bubble(n, data):
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                tmp = data[j]
                data[j+1] = data[j]
                data[j] = tmp
    for i in range(n):
        print(data[i], end = " ")

n = int(input("정렬 수 입력:"))
data = list(map(int, input().split()))



    
