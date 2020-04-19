#open06_2

#10 미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9 이다. 이들의 총 합은 23 이다
#1000 미만의 자연수에서 3의 배수와 5의 배수의 총 합을 구하라

result = 0
for i in range(1,1000):
    if i % 3 == 0 or i%5==0:
        result += i

print(result)

    
