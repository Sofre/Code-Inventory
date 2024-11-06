import bisect
def index_left(a,x):
    i=bisect.bisect_left(a,x)
    return i

def index_right(a,x):
    i = bisect.bisect_right(a,x)
    return i


a = [1,2,3,4]
print(index_left(a,2))
print(index_right(a,2))
    