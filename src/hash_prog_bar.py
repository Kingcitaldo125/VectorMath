import math

hash_mark = "#"
start = 7
finish = 10
size = 30



perc = (start/finish)*100
perc_dec = start/finish
cur_size = perc_dec*size
space_buffer = size-perc_dec

print("{" + "#"*int(cur_size) + " "*int(size-cur_size) + "}")
print(cur_size)