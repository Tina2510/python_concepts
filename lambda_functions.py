'''without giving name to lambda function'''
res = (lambda num,p : num**p)(2,5) #lambda function arguments : exp 
print(res)

''' giving a name to lambda function'''
fun = lambda num,den : num/den 
res = fun(10,2)
print(res)