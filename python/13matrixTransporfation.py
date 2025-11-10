import numpy
def translation():
    Tx=int(input("Enter the Tx value : "))
    Ty=int(input("Enter the Ty value : "))
    return numpy.matrix([[1,0,Tx],[0,1,Ty],[0,0,1]])
def rotation():
    degree=int(input("Enter the degree : "))
    theta=numpy.radians(degree)
    cos=numpy.cos(theta)
    sin=numpy.sin(theta)
    return numpy.matrix([[cos,sin,0],[sin,cos,0],[0,0,1]])

def scaling(sx=0,sy=0):
    return numpy.matrix([[sx,0,0],[0,sy,0],[0,0,1]])
print("\n Translation : \n",translation())
print("\n Rotation : \n",rotation())
print("\n Scaling : \n",scaling())