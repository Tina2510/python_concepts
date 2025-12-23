from functools import reduce
'''using def'''
lst = [1,2,3,4,5]

def fun(x,y):
    return x+y

res = reduce(fun,lst)
print(res)

'''using lambda function'''

lst2 = [1,2,3,4,5]
res = reduce(lambda x,y : x+y, lst2)
print(res)