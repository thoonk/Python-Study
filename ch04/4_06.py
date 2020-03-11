input_string = input("입력:")

f=open("test1.txt", 'a')
f.write(input_string)
f.write('\n')
f.close()