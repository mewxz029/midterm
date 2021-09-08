vowel = ['a','e','i','o','u']

def checkVowel():
    rawString = input("Enter some text: ").lower()
    for s in rawString:
        for i in vowel:
            if (s is i):
                return print("There is vowel")
    return print("There is not vowel")

checkVowel()