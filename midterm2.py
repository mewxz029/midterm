import statistics 
# ฟังก์ชันรับค่ามาหลายๆค่า แล้วแปลงเป็น list
def inputNumber():
    # map(fun, iter)
    # map(int => แปลงให้ str ที่รับเข้ามาเป็น int, ข้อมูลที่ input เข้ามา)
    number = list(map(int, input("Enter a list of number: ").split()))
    return number

def checkAMM(listnumber):
    avg = sum(listnumber) / len(listnumber)
    med = (len(listnumber) + 1) / 2
    # find mode
    set_list = set(listnumber)
    set_list = list(set_list)
    dict_dup = {}
    for i in set_list:
        dict_dup[i] = 0
    
    for j in set_list:
        for k in listnumber:
            if (j == k):
                dict_dup[j]+=1

    dict_key = dict_dup.keys()
    dict_value = dict_dup.values()

    key = []
    for x in dict_key:
        key.append(x)
    
    value = []
    for x in dict_value:
        value.append(x)

    max_dup = max(value)
    mod = []
    for i in range(len(value)):
        if (value[i] == max_dup):
            mod.append(key[i])

    return avg, med, mod
           
listnumber = inputNumber()
avg, med, mod = checkAMM(listnumber)

print("ค่าเฉลี่ย : " + str(avg))
print("ค่ามัธยฐาน : " + str(med))
# ฐานนิยมมีมากกว่า 1 ตัว
print("ค่าฐานนิยม: ", *mod, sep = " ")
