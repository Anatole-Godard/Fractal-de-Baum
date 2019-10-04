from turtle import*
speed(0)
 
def arbre(long,n):
    if n==0:
        color("brown")
        forward(long)
        pencolor('green')
    else:
        arbre(long,n-1)
        right(30)
        arbre(long,n-1)
        backward(long)
        left(30)
        arbre(long,n-1)
        backward(long)
        left(30)
        arbre(long,n-1)
        backward(long)
        right(30)
        backward(long)
        arbre(long,n-1)
left(90)
for k in range(5):
    arbre(50,5)
