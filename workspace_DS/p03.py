f=open("test.txt", "r")
content=f.read()
f.close()

content = content.replace('java', 'python')
print(content)
f=open("test.txt", "w")
f.write(content)
f.close()