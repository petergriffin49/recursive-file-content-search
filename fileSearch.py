import os
import time

folderQueue = []
files = []
instances = {}
searchQuery = input("Enter the string to search for: ").lower().strip()
rootPath = input("Enter the root folder's address: ")
t0 = time.time()

# (recursive) add folders and files in a folder
def addFiles(directory):
    contentList = os.listdir(directory)
    for file in contentList:
        myPath = directory + "\\" + file
        if os.path.isfile(myPath):
            files.append(myPath) # single file
        elif os.path.isdir(myPath):
            addFiles(myPath) # (recursive) another folder

# execute file collection
addFiles(rootPath)
filesTotal = len(files)

# search every files for phrase
myString = ""
while len(files) > 0:
    file = files.pop()
    fileOpen = open(file, 'r')
    lineI = 0
    while True: # every line in the current file
        try:
            myString = fileOpen.readline()
        except(UnicodeDecodeError):
            break
        if not myString:
            break
        myString.lower()
        if searchQuery in myString:
            lineList = instances.get(file,[])
            lineList.append(lineI+1)
            instances.update({file : lineList})

        lineI += 1
    fileOpen.close()


# print results
if len(instances) == 0:
    print()
    print("No instances of "+ searchQuery +" found!")
else:
    print()
    print('Instances of "' + searchQuery + '" in ' + rootPath +':')
    lines = []
    for key in instances:
        if len(instances[key]) > 1:
            listStr = ""
            ii = 0
            for i in instances[key]:
                ii += 1
                if ii > 1:
                    listStr += ", "
                listStr += str(i) 
                
            print("In " + key + " on lines " + listStr)
        else:
            print("In " + key + " on line " + str(instances[key][0]))
    print()

print("Searched through " + str(filesTotal) + " files in "+str(round(time.time()-t0,2))+" seconds.")
