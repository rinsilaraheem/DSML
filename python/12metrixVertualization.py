import numpy
data1=numpy.matrix([[1,2,5],[3,4,8],[4,2,6]])
data2=numpy.matrix([[2,3,6],[4,7,9],[2,2,6]])
add=numpy.add(data1,data2)
print("Addition : \n",add)
sub=numpy.subtract(data1,data2)
print("Subtraction : \n",sub)
mul=numpy.multiply(data1,data2)
print("Multiplication : \n",mul)
tra=numpy.transpose(data1)
print("Transpose of first matrix : \n",tra)
scalarmul = data1 * 2
print("Scalar multiplication first matrix with 2 : \n",scalarmul)