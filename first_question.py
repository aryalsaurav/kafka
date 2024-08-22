### what should be done is
# (P,Q) is indices
# so p should be less that q but A[q] should be less that A[p]


def solution(a):
    count = 0
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[j] < a[i]:
                count +=1
    return count if count < 1_000_000_000 else -1


a_list = [-1,6,3,4,7,4]

b = solution(a_list)
