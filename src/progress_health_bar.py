import math

currenthp = 99
maxhp = 100
guague_size = 40


form1 = currenthp/maxhp
form2 = guague_size * form1
finish_bar = (guague_size)-int(form2)

bar1 = ("/" +  ("-"*guague_size) + ("\\"))
bar2 = ("|" + ("+" * int(abs(form2))) + ((" " * int(finish_bar) + ("|"))))
bar3 = ("\\" + ("-"*guague_size) + "/")


print(bar1)
print(bar2)
print(bar3)

print(form1)