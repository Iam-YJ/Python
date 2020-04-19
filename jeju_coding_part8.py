#jeju_coding_part8(71~80)

#71
#72
#73
#74

#75
data = input("숫자 입력 : ")

datai = int(data)
d = []
count = 0

for i in range(datai+1):
    d.append(str(i))
    if d[i].count('3') or d[i].count('6') or d[i].count('9'):
        count +=1

print(count)


