A = [13,27,35,40,49,55,59]
B = [17,35,39,40,55,58,60]
i,j = 0,0
end = len(A)
while(i < end and j < end):
    #Linear Search
    print(A[i],B[j])
    if A[i] < B[j]:
        i+=1
    else:
        if A[i] == B[j]:
            print(True)
            i+=1
        j+=1
