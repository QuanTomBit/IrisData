import re

file = open('iris.txt', 'rU')

irises = {}

for line in file:
    match = re.search(r'[\w.\w,\w.\w,](\w\.\w),.+,(\w+\-\w+$)', line)

    if match:
        species = match.group(2)
        petal_length = float(match.group(1))
        irises.setdefault(species, [0, 0])
        irises[species][0] += 1
        irises[species][1] += float(petal_length)

file.close()

for key in irises:
    print('Amount of ' + key +': ' + str(irises[key][0]))

    average = irises[key][1] / irises[key][0]
    print(' Average petal length: {0:.2f}'.format(average))
    
