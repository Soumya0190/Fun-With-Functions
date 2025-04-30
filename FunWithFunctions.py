import math
def cylinderVolume(radius, height):
    V = (math.pi) * radius * radius * height
    return V
def formatNumber(number):
    return "{:,}".format(number)
def securePassword(password):
    countU = 0
    countL = 0
    countN = 0
    countS = 0
    if len(password) >= 8:
        for char in password:
            if char.isupper():
                countU += 1
            elif char.islower():
                countL += 1
            elif char.isdigit():
                countN += 1
            else:
                countS += 1
        if ((countU >= 1) and (countL >= 1) and (countN >= 1) and (countS >= 1)): 
            return True
    return False
def middleValue(a, b, c):
    lst = [a, b, c]
    lst.sort()
    return lst[1]
def isBinary(number):
    number2 = str(number)
    count = 0
    for num in number2:
        if num == '0' or num == '1':
            count += 1
    if count == len(number2):
        return True
    return False
def scramble(phrase):
    lst = []
    keys = {'Q':'W', 'W':'E', 'E':'R', 'R':'T', 
    'T':'Y', 'Y':'U', 'U':'I', 'I':'O', 'O':'P', 
    'P':'Q', 'A':'S', 'S':'D', 'D':'F', 'F':'G',
    'G':'H', 'H':'J', 'J':'K', 'K':'L','L':'A',
    'Z':'X', 'X':'C', 'C':'V', 'V':'B', 'B':'N',
    'N':'M', 'M':'Z', ' ': ' '}
    for char in phrase:
        letter = keys[char]
        lst.append(letter)
    word = "".join(lst)
    return word
def removeChars(phrase, remove):
    for char in remove:
        if char in phrase:
            phrase = phrase.replace(char,"")
    return phrase
def isPalindrome(phrase):
    phrase2 = phrase.replace(" ","")
    phrase2 = phrase2.lower()
    rvs = phrase2[::-1]
    if phrase2 == rvs:
        return True
    return False







