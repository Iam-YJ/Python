#jeju_coding_part3(21~30)

#21

#22

#23

#24
name = input("이름 : ")

print(name.upper())

#25
r = int(input("반지름 : "))

print(r*r*3.14)

#26

sunFamily ={'수성':'Mercury','금성':'Venus','지구':'Earth','화성':'Mars','목성':'Jupiter','토성':'Saturn',
            '천왕성':'Uranus','해왕성':'Neptune'}

select = input("행성을 선택하세요 : ")
print(sunFamily[select])


#27
keys = input("이름 : ").split()
values = map(int, input("점수 : " ).split())

result = dict(zip(keys, values))
print(result)


#28
data = input("글자를 입력하세요 : "  )

for i in range(len(data)-1):
    print(data[i], data[i+1], sep=" ")
    

#29

alphabet = input("알파벳을 입력하세요 : ")

if alphabet >= 'A' and alphabet <='Z' :
    print("YES")
else:
    print("NO")


#30
string = input("문장을 입력하세요 : ")
find = input("찾을 문자를 입력하세요 : ")

result = string.find(find)
print(result)




    
