import os
class IV():
     def getIVlist(filename, sheetname):
        with open(filename, 'r') as file:
            wholeFile = file.read()
            data = wholeFile.split('**Data**')[1]
            #print(data)

            splitted = data.split()

            v = []
            i = []

            if str(filename).endswith('drk'):
                jump = 3
            else :
                jump = 4

            for j in range(0, len(splitted),jump):
                v.append(splitted[j])
                i.append(splitted[j+1])

            #print(v)
            #print(i)

            iv = [v, i]

            return iv