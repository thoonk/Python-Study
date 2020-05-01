def getPage(total, onePage):
    if total%onePage==0:
        return total//onePage
    else:
        return total//onePage+1


print (getPage(5,10))
print (getPage(15,10))
print (getPage(25,10))
print (getPage(30,10))