def myfunc(a,b):
    c = a * b
    print(c)
myfunc((1,2,3),4)
myfunc(1,2)
myfunc(1.0,2)
myfunc([1],2)
myfile = open('barcodes.txt', 'r')
data = list(myfile)
print(data)
