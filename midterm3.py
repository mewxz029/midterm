vowel = ['a','e','i','o','u']

def checkVowel():
    rawString = input("Enter some text: ").lower()
    for s in rawString:
        for i in vowel:
            if (s is i):
                return print("There is vowel")
    return print("There is not vowel")

def checkVowelNew():
    rawString = input("Enter some text: ").lower()
    for i in vowel:
        if i in rawString:
            return print("There is vowel")
    return print("There is not vowel")

checkVowelNew()