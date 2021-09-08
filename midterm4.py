# หาจำนวนเฉพาะ
# มีแค่ 1 และตัวมันเองที่หารลงตัว

def inputNumber():
    # map(fun, iter)
    # map(int => แปลงให้ str ที่รับเข้ามาเป็น int, ข้อมูลที่ input เข้ามา)
    number = list(map(int, input("Enter a list of number: ").split()))
    return number

def primeNumber(x):
    # 1 ไม่ใช่จำนวนเฉพาะ
    if (x >= 2):
        for y in range(2, x): # range(2, x) => 2 ถึง x - 1
            if not (x % y): # check ว่าหารลงตัวไหม ถ้าหารลงตัวจะรีเทิร์นเป็น True แล้วเข้าเงื่อนไข
                return False
    else: # not 1 and 0
        return False
    return True

def checkList(list):
    boollist = []
    for i in list:
        boollist.append(primeNumber(i))
    return boollist

listnum = inputNumber()
boollist =checkList(listnum)
print(boollist)
# checkList([2,3,5,7,11,13,23,15])

