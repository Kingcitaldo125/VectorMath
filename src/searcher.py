#string regex matcher and line printer
import os

def matchmaker(result,key,file):
    if result:
        print("Found",key,"in",file)
    else:
        return

def match(stringone,stringtwo):
    #x=0
    lenone = len(stringone)
    lentwo = len(stringtwo)

    compareone=""
    ctr = 0
    for x in range(len(stringtwo)):
        if stringone[ctr]==stringtwo[x]:
            g=0
            while g < lenone:
                if stringone[g]==stringtwo[x+g]:
                    #print("Got",stringone[g],"with",stringtwo[x+g])
                    compareone+=stringone[g]
                else:
                    compareone=""
                    g=0
                    break
                g+=1

    #print("result:",compareone)
    if compareone==stringone:
        return True
    return False

def readLine():
    print("line.\n")
    
def searchFile(filename,extention,key):
    fobj = ''
    data = {}
    position = 's'
    lctr = 1
    
    fobj = open(filename,"r+")
    foo = open(filename,"r+")
    
    position = fobj.tell()
    if extention == "txt" or extention == ".tx" or extention == ".txt":
        print("Currently processing "+str(filename))
        print("\n")

        for f in foo:
            data[str(lctr)] = f
            lctr+=1
                
        lctr=1
        for xx in fobj:
            xxx = str(xx)
            mth = match(key,xxx)
            if mth:
                print('in',filename,':\n',data[str(lctr)])
            lctr+=1
                
    fobj.close()
    foo.close()


def main():
    #Search the current directory
    stack = []
    curfile = 0
    direc = os.getcwd()
    print("Current working directory:",os.getcwd())

    key = str(input("Enter string to search for:\n"))
    #key = str(key)

    for e in os.listdir(direc):
        #print("File Name:",e)
        extention=""
        last = e[len(e)-1]
        slast = e[len(e)-2]
        tlast = e[len(e)-3]
        extention+=tlast
        extention+=slast
        extention+=last
        
        
        #print("File Extention: ",extention)
        #print("\n")

        searchFile(e,extention,key)


main()
        
#xd = "This offends me as a vegan transgender atheist who vapes and crossfits\
#You're 4 times a week and im also a male feminist as I identify myself as a pastafarian"
#xx = match("pas",xd)
#matchmaker(xx,"pas",xd)

#x = match("paul","There was a small boy named pauli in hte suburbs")
#matchmaker(x,"paul","There was a small boy named pauli in hte suburbs")

#m = match("helicopter","There was a giant helicopter")
#print(m,'\n')

#x = match("last","This is the last time that I do it")
#print(x,'\n')
