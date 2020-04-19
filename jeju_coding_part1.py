#python_jeju coding base camp

#01
nums=[100,200,300,400,500]

nums.remove(400)
nums.remove(500)

print(nums)

#02
l = [200,100,300]
l.insert(2,10000)
print(l)

#03
l=[100,200,300]
print(type(l))

#의 정답은? 3(list)

#04
a='p'
print(type(a))
#의 정답은? 3(str)

#05
a=10
b=2
for i in range(1,5,2):
    a += i

print(a+b)

#답은 16 - 왜? 10 > 11 > 14 >> 14+2 >> 16


#06
#답은 1 True

#07
#as 는 변수 명으로 사용 못함
#1age 도..

#08
d={'height':180, 'weight':78,'weight':84,'temparture':36,'eyesight':1}
print(d['weight'])
# 84가 출력된다 - 딕셔너리에서 키가 중복되면 값이 제일 나중에 들어간게 나옴

#09
year='2019'
month='04'
day='26'
hour='11'
minute='34'
second='27'

print(year, month, day, sep="/", end=' ')
print(hour, minute, second, sep=":")

#10
t = int(input("트리 몇 줄? : "))

for i in range(1,t+1):
    for j in range(t+1-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()




