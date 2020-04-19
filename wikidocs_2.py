#wikidocs_2

#10

class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList

    def sum(self):
        result = 0
        for i in self.numberList :
            result += i
        return result

    def avg(self):
        total = self.sum()
        return total / len(self.numberList)

    
#12
# 정답은 7

#15
def checkNum(s):
    result =[]
    for num in s:
        if num not in result:
            result.append(num)
            
        else:
            return False
    return len(result) == 10


#17
#답은 2번


    
