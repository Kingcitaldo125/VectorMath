rows = ["0","0","0"]
cols = ["0","0","0","0","0"]



for col in cols:
    if len(cols) > 2:
        s = "/" + str(rows) + "\\"
        s + "|" + " " + "|"
        s + "\\" + str(cols) + "/"
    else:
        s = "/" + str(rows) + "\\"
        s + "\\" + str(cols) + "/"
    print(s)