from display import *
from draw import *
from matrix import *
import random

#Testing
m2=new_matrix(0,0)
add_edge(m2,1,2,3,4,5,6)
print_matrix(m2)

m1=new_matrix()
ident(m1)
print_matrix(m1)


m3=matrix_mult(m1,m2)
print_matrix(m3)

m4=new_matrix(0,0)
add_edge(m4,1,2,3,4,5,6)
add_edge(m4,7,8,9,10,11,12)
print_matrix(m4)

m5=matrix_mult(m4,m2)
print_matrix(m5)


screen = new_screen()
color = [ 255, 0, 255 ]

edgeMatrix=new_matrix()
for x in range(50):
    x0=random.randint(1,500)
    y0=random.randint(1,500)
    for y in range(10):
        x1=random.randint(-20,10)-x0
        y1=random.randint(-20,10)-y0
        add_edge(edgeMatrix,x0,y0,0,x1,y1,0)


draw_lines( edgeMatrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
