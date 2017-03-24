def __blah__(x):
    """Blah Blab, blah """
    empty_blah = []
    if isinstance(x,int):
        return str("BLAH "*x)
    elif isinstance(x,str):
        return str("BLAH.")
    elif isinstance(x,list):
        empty_blah.append(x)
        return empty_blah
    else:
        raise TypeError("MUST PASS BLAH")

x = __blah__(10)
y = __blah__("blah")

print(x)
print(y)