# This function takes 2 matricies (as lists of lists)
# and performs matrix multiplication on them.
# Note: you may not use any matrix multiplication libraries.
# You need to do the multiplication yourself.
# For example, if you have
#     a=[[1,2,3],
#        [4,5,6],
#        [7,8,9],
#        [4,0,7]]
#     b=[[1,2],
#        [3,4],
#        [5,6]]
#  Then a has 4 rows and 3 columns.
#  b has 3 rows and 2 columns.
#  Multiplying a * b results in a 4 row, 2 column matrix:
#  [[22, 28],
#   [49, 64],
#   [76, 100],
#   [39, 50]]
from datetime import datetime
import random
import time
# generate a random array of size size1 x size2
def genArr(row,clm):
    arr = []
    for i in range(row):
        row = []
        for j in range(clm):
            row.append(random.randrange(0,10))
        arr.append(row)
    return arr


# matrix multiplication
def matrix_mul(a,b):
    # Write me
    res = [[0]*len(b[0]) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum += a[i][k] * b[k][j]
            res[i][j] = sum
            
    return res





if __name__ == "__main__":
    # initialize the sizes array
    sizes = []
    count_n = 4
    while(count_n <= 512):
        sizes.append(count_n)
        count_n *= 2
    # print sizes
    for i in range(len(sizes) - 1):
        print("%7d" %sizes[i],",",sep="",end="")
    print("%7d" %sizes[-1])

    # Many rows by few columns (N*4)xN * Nx(N/4)
    times = []
    
    for size in sizes:
        a = genArr(size * 4,size)
        b = genArr(size,int(size / 4))
        start = time.perf_counter()
        matrix_mul(a,b)
        end = time.perf_counter()
        times.append(end - start)

    for i in range(len(times) - 1):
        print("%2.5f" %times[i],",",sep="",end="")
    print("%2.5f" %times[-1])

    # Square NxN * NxN
    times = []
    
    for size in sizes:
        a = genArr(size, size)
        b = genArr(size, size)
        start = datetime.now()
        matrix_mul(a,b)
        times.append((datetime.now()-start).total_seconds())

    for i in range(len(times) - 1):
        print("%2.5f" %times[i],",",sep="",end="")
    print("%2.5f" %times[-1])

    # Few rows by many columns (N/4)xN * Nx(N*4)
    times = []
    
    for size in sizes:
        a = genArr(int(size/4), size)
        b = genArr(size, size * 4)
        start = datetime.now()
        matrix_mul(a,b)
        times.append((datetime.now()-start).total_seconds())

    for i in range(len(times) - 1):
        print("%2.5f" %times[i],",",sep="",end="")
    print("%2.5f" %times[-1])


    