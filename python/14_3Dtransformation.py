import numpy
def translation():
    Tx=int(input("Enter the Tx value : "))
    Ty=int(input("Enter the Ty value : "))
    Tz=int(input("Enter the Tz value : "))
    return numpy.matrix([[1,0,0,Tx],[0,1,0,Ty],[0,0,1,Tz],[0,0,0,1]])
def rotation():
    degree=int(input("Enter the degree : "))
    theta=numpy.radians(degree)
    cos=numpy.cos(theta)
    sin=numpy.sin(theta)
    return numpy.matrix([[1,0,0,0],[0,cos,-sin,0],[0,sin,cos,0],[0,0,0,1]])

def scaling(sx=0,sy=0,sz=0):
    return numpy.matrix([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]])
print("\n Translation : \n",translation())
print("\n Rotation : \n",rotation())
print("\n Scaling : \n",scaling())