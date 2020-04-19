#jeju_coding_part4(31~40)

#31 - 답 3


#32
data = input("문자열을 입력하세요 : ")

l = list(data.split())
print(len(l))


#33
data = input("숫자를 입력하세요 : ")
print(''.join(reversed(data)))


#34
data = list(map(int, input("키를 입력하세요 : ").split()))

data2 = sorted(data)
            
if data == data2:
    print("YES")
else:
    print("NO")
    

#35
def one(n):
    def two(r):
        result = r **n
        return result
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))


#36
data = input("? 단을 입력하세요:")

for i in range(1,10):
    print(int(data)*i, end=' ')
print()


#37
data = list(map(str,input("반장 입력 : ").split()))
count = 0
for i in range(len(data)):
    if data.count(data[i-1]) < data.count(data[i]):
        count = i
print(f"{data[count]}이가 총 {count}표로 반장이 되었습니다.")


#38
user_input = input("점수 입력 : ")

l = list(user_input.strip().split())
l = [int (i) for i in l]

count = 3
#3개는 무조건 구매, 배열 정렬 후 1~3위 중 중복되는 숫자까지 포함

data_sorted = sorted(list(l))
print(data_sorted)

for i in range(len(l)-1):
    for j in range(len(l)-1):
        if data_sorted[i] == data_sorted[j]:
            count += 1
    j+=1


#39
data = input("문자를 입력하세요 : ")

ndata = data.replace('q','e')
print(ndata)

#40

limit = int(input("제한 무게 : "))
people = int(input("사람 수 : "))
total = 0
count = 0

for i in range(people):
    if total <= limit:
        total += int(input("무게 : "))
        count = i
    else:
        break
print(count)
    
    


        



