def is_pair(A,N,X):
    for i in range(N):
        for j in range(N):
            if(i==j):
                continue
            if(A[i] + A[j] == X):
                return(A[i] ,A[i])
            if (A[i]+A[j]<X):
                break

    return 0

arr = [1,5,2,6,4,8,5,8,4,7,4,6,5,3,8,4,6,42,4,7,2,4,5,3,6,8,4,3,4,6,34,7,4]
val = 1253
print("pair: {} {}".format(val, is_pair(arr,len(arr), val)))

def is_pair_smells(A,N,X):
    i = 0
    j = N -1
    while(i < j):
        if(A[i] + A[j] == X):
            return[A[i], A[j]]
        if (A[i]+A[j]<X):
            i += 1

arr = [1,5,2,6,4,8,5,8,4,7,4,6,5,3,8,4,6,42,4,7,2,4,5,3,6,8,4,3,4,6,34,7,4]
val = 12
print("pair: {} {}".format(val, is_pair(arr,len(arr), val)))
        






























