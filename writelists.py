import csv

## Enter lists with values to be wriiten to csv file
s = [5,3,6,2,1]
w = [1,3,2,2,1]
    
## Creates new csv file
a = open("3.csv","wb") 

with open("3.csv", "w+") as t:
    p= csv.writer(t, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    p.writerow(s)
    p.writerow(w)
