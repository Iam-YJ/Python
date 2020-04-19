#jeju_coding_part2 (11~20)

#11
s=0

for i in range(1,101):
    s+=i

print(s)

#12
class Wizard():
    def __init__(self,health,mana,amor):
        self.health = health
        self.mana = mana
        self.amor = amor

    def attack(self):
        print("파이어볼~")

#x = Wizard(545,210,10)

#13
sunFamily = ["","수성","금성","지구","화성","목성","토성","천왕성","해왕성"]

#14
def three(n):
    if n % 3 ==0 :
        print("짝")
    else:
        print(n)

#15
name = input("이름이 뭐야? : ")
print("제 이름은 %s입니다" %name)
#print('안녕 내 이름은 {} 입니다'.format(name))

#16
r = input("입력 : ")

s_reverse = ''
for char in r:
    s_reverse = char + s_reverse

print(s_reverse)

#print(n[::-1])


#17
play = int(input("키 : "))

if play >= 150:
    print("YES")
else:
    print("NO")


#18
data = list(map(int, input("성적:").split()))

print(int(sum(data)/3))


#19
a, b= list(map(int, input("수 계수 : ").split()))

result = 1
for i in range(b):
    result *= a
print(result)

#n = list(map(int, input().split()))
#print(n[0] ** n[1])


#20
data = list(map(int, input("나눌래 뭐로?").split()))

print(data[0]//data[1] ,data[0] % data[1])
