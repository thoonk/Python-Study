f=open("test2.txt", "r")
content=f.read()
f.close()

content = content.replace('java', 'python')
f=open("test2.txt", "w")
f.write(content)
f.close()