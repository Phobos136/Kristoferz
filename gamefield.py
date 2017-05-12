col = 7
row = 6

#field = [[]]
field = [[i * j for j in range(col)] for i in range(row)]
#print(field[i][j])
for i in range(row):
    for j in range(col):
        field[i][j] = 0
for n in field:
     print(' '.join([str(elem) for elem in n]))
        #print(field[i][j])
