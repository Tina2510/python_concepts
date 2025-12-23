'''withput using lambda function'''
lst = [10,13,18,15,20]
def fun(x):
    if x%2 == 0:
        return True
    else:
        return False
    

evn_lst = list(filter(fun,lst))
print(evn_lst)

'''using lambda function'''
lst =[10,13,18,15,20]

result = list(filter(lambda x : (x%2 == 0), lst))
print(result)
