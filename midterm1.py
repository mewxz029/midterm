# ฟังก์ชันรับค่ามาหลายๆค่า แล้วแปลงเป็น list
def inputNumber():
    # map(fun, iter)
    # map(int => แปลงให้ str ที่รับเข้ามาเป็น int, ข้อมูลที่ input เข้ามา)
    number = list(map(int, input("Enter a list of number: ").split()))
    return number

def checkMinMax(list):
    maxValue = max(list)
    minValue = min(list)
    return minValue, maxValue

listnumber = inputNumber()
minValue, maxValue = checkMinMax(listnumber)



print("minValue :" + str(minValue))
print("maxValue :" + str(maxValue))
