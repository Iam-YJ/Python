#jeju_coding_part6(51~60)

#51
data = [180, 145, 165, 45, 170, 175, 173, 171]

def merge_sort(data):
    size = len(data)
    if size <= 1:
        return data
    mid = size // 2
    sort1 = merge_sort(data[:mid])
    sort2 = merge_sort(data[mid:])
    result = []

    while (sort1) and (sort2) :
        if (sort1[0] < sort2[0]):
            result.append(sort1.pop(0))
        else:
            result.append(sort2.pop(0))

    while sort1:
        result.append(sort1.pop(0))
    while sort2:
        result.append(sort2.pop(0))
    return result

print(merge_sort(data))

#52

data = [180, 145, 165, 45, 170, 175, 173, 171]

def quick_sort(data):
    size = len(data)
    if size <= 1:
        return data
    pivot = data.pop(len(data)//2)
    sort1 = []
    sort2 = []
    
    for i in range(size-1):
        if data[i] < pivot :
            sort1.append(data[i])
        else:
            sort2.append(data[i])
    return quick_sort(sort1) + [pivot] + quick_sort(sort2)

print(quick_sort(data))


#53
data = list(map(str, input("문자열 입력:")))

small = ['(',')']
mid = ['{','}']
large = ['[',']']

print(data)
if data == small or data == mid or data == large:
    print('YES')
else:
    print('NO')

#54
data = list(map(int,input("5개 숫자 입력:").split()))
confirm = []

max = max(data)

for i in range(5):
    confirm.append(max-i)
    
if sorted(data) == sorted(confirm):
    print("YES")
else:
    print('NO')

#55

#56
nationWidth = {'korea': 220877,'Rusia': 17098242,'China': 9596961,
               'France': 543965,'Japan': 377915,'England' : 242900 }
width = []
country=[]

del(nationWidth['korea'])

for value in nationWidth.values():
    width.append(value)

for key in nationWidth.keys():
    country.append(key)

for i in range(len(width)):
    width[i] = abs(width[i] - 220877)
    mini = min(width)
    
for i in range(len(width)):
    if(mini == width[i]):
        print(country[i], mini)

#57
def count(n):
    countN = str(list(range(n+1))).count('1')
    return countN
print(count(1000))


#58

data = int(input("정산 금액:"))

result=format(data,',')
print(result)

#59
str = input("문자 입력:")
print("{:=^50}".format(str))

#60
student = ['강은지','김유정','박현서','최성훈','홍유진','박지호',
           '권윤일','김채리','한지호','김진이','김민호','강채연']

s=sorted(student)
count = 0

for i in range(len(s)):
    count += 1
    print(f"번호: {count}, 이름: {s[i]}")

    
