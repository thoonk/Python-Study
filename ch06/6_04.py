import sys

#sys.argv[0] 입력받는 값

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()

#python 6_04.py -a "write something"