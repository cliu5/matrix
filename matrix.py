"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
'''
total = ""
    for i in range(4):
        for row in matrix:
            total += str(row[i]) + " "
        total += "\n"
    print(total)
'''
def print_matrix( matrix ):
    curr=[]
    newMatrix=''
    for x in range(4):
        for y in matrix:
            #print(x)
            #print(y)
            newMatrix+= str(y[x])
            newMatrix+= ' '
        newMatrix+= '\n'
    print(newMatrix)
    '''
    newMatrix=[]
    counter=1
    for individuallist in matrix:
         for element in individuallist:
             if individuallist.index(element)%counter==0:
                 curr=[]
                 curr.append(element)
         counter+=1
         newMatrix.append(curr)
    print(newMatrix)
'''
#testMatrix=[[1,2,3,1],[2,3,4,1],[3,4,5,1]]
#print(print_matrix(testMatrix))
#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if x==y:
                matrix[x][y]=1
            else:
                matrix[x][y]=0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    newMatrix=new_matrix(4,len(m2))
    if (len(m1)) != (len(m2[0])):
        print("Undefined")
    else:
        counter=0
        while counter<4:
            for x in range(len(m2)):
                ans=0
                for y in range(len(m1)):
                    ans+=m1[y][counter]*m2[x][y]
                newMatrix[x][counter]=ans
            counter+=1
    return newMatrix



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
