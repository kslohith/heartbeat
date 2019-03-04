w =[]
with open("1.csv") as f:
    for line in f:
        for word in line.split():
            w.append(word)
            
a = open("3.txt","wb") 
a.close()

with open("3.txt", "w+") as t:
    for x in w:
        t.write(x + ",")
