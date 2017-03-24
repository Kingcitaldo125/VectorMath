import random

stringss = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ,'I', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nums = ['1','2','3','4','5','6','7','8','9','0']

i = 0
res = ""
while i < 5:
    f = random.randrange(0,2)
    if f == 1:
        ff = random.randrange(0, len(stringss)-1)
        ac = stringss[ff]
        res += ac
    else:
        ff = random.randrange(0, len(nums)-1)
        ac = nums[ff]
        res += ac
    i += 1
print(res)
