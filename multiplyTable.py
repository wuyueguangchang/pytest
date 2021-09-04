'''
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
'''
for row in range(1,10):
    for col in range(1,row+1):
        print('{col}*{row}={colRow}'.format(col=col,row=row,colRow=col*row),end='\t')
    print()