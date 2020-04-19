#01

a= 'a:b:c:d'
b = a.split(":")
c="#".join(b)
print(c)
print()

#02
a={'A':90, 'B':80}
a.update(C=70)
print(a['C'])
print()

#03
#list에 + 를 써서 추가하면 새로운 리스트가 반환되고(새로운 주소값)
#list에 extend를 써서 추가하면 기존 리스트가 반환된다(주소값 안변함)

#04
A=[20,55,67,82,45,33,90,87,100,25]

result = 0
for i in range(0,10):
    if A[i] >= 50 :
        result += A[i]
print(result)
print()

#05
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
for i in range(1,10):
    print(fib(i))
print()

#06
user_input = input("숫자를 입력하세요: ")
numbers = user_input.split(",")

result = 0

for n in numbers:
    result += int(n)
    
print(result)
print()


#07
user_input = input("구구단을 출력할 숫자를 입력하세요(2~9): ")
n = user_input

for i in range(1,10):
    print(int(n)*i, end=' ')

#10 아직 못품 ㅜㅜ

#13

#14
    
