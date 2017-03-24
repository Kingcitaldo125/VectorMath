#Palindrome test

def palindromes(word):
    """ Returns a boolean"""
    for i in word:
        temps1 = i
    for i in word[::-1]:
        temps2 = i
    if temps1 == temps2:
        return True
    else:
        return False


string1 = "tacocat"#true
string2 = "hello"#false
string3 = "stanleyyelnats"#true
mytest = palindromes(string1)
my2nd = palindromes(string2)
my3rd = palindromes(string3)

print(mytest)
print(my2nd)
print(my3rd)