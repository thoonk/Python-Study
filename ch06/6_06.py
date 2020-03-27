import os

def search(dirName):
    try:

        fileName = os.listdir(dirName)
        for f in fileName:
            all_fileName = os.path.join(dirName, f)
            if os.path.isdir(all_fileName):
                search(all_fileName)
            else:
                extend = os.path.splitext(all_fileName)[-1]
                if extend == '.py':
                    print(all_fileName)
    except PermissionError:
        pass

search("your path")


