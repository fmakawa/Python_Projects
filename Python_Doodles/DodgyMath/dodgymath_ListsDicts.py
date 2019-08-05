import csv

#########################################################  Global Variables ############################################
data = dict()
dates = []
numbers = []
#Frequency of Values
count70 = dict()
count140 = dict()
count210 = dict()
count280 = dict()
count3500 = dict()

#Format initial download document. Remove unneeded rows
with open('dodgy.csv') as in_file:
    with open('dodgy2.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        readCSV = csv.reader(in_file, delimiter=',')
        for row in readCSV:
            if row and readCSV.line_num>1:
                writer.writerow(row)


#Read data from document and populate variables.
with open('dodgy2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    
    for row in readCSV:
        i=readCSV.line_num
        """
        b=list(row)
        print (type(b))
        print (len(b))
        print (b)
        date = b[0]
        print (i)
        """
        data[i] = {'date':row[0],'numbers':row[1:8],'reintegro':row[-1]}
        numbers.extend(row[1:8]) #Use extend since that simples adds the values as new values to the exisitng list. If you use append it will add this as a nested list into the existing list


    def countingvalues(ls,n):
        dicky = dict()
        numberscounted = 0
        ls = ls[:n+1]
        print (ls)
        print (len(ls))
        i=1
        total =0
        while i <50:
            dicky[str(i)]=ls.count(str(i))
            numberscounted +=1 
            i +=1
            total += ls.count(str(i))
        
        print(dicky)
        print (total)
        print (numberscounted)
        return dicky
    
    countingvalues(numbers,70)

    #print (data)
    #print (len(numbers))
