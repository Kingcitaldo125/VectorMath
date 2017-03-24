#automata lab 1
import cmd;
import sys,re;
import os;
current = os.getcwd();
data = open("letter.txt").read()

x = input("What String?");

rex = re.compile(r"(?i)x")
secrex = re.findall(r"(?i)paul")
m = rex.search(txt)
n = secrex.search(txt)

if m:
    print("Matched:",m.group(0))
else:
    print("Match:",n.group(0))