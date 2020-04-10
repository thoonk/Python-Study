#OX퀴즈
n = int(input())
output_lst=[]
for i in range(n):
   score = 0
   cnt = 0
   ox = input()
   for j in range(len(ox)):
       if ox[j]=='O':
           cnt += 1
           score += cnt
       elif ox[j] == 'X':
           cnt = 0
   print(score)






