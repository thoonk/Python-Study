#list = [1,-2,3,-5,8,-3]

def positive(list):
    result=[]
    for i in list:
        if i>0:
            result.append(i)
    return result


print(list(filter(lambda i:i>0, [1,-2,3,-5,8,-3])))

#print(positive(list))
