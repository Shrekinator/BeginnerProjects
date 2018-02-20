#get number of files
try:
    FileNum = int(input("How many files to read?: "))
except TypeError:
    print("Please input integers only")

#set variables and create list to store directories
FilesDir = []
FilesCont = []

#user inputs directories into list
for i in range(FileNum):
    FilesDir.append(input("Directory for File #"+str(i+1)+": "))

print(FilesDir)

#reads each file
for i in range(len(FilesDir)):
    file = open (FilesDir[i], "r")
    content = file.read()
    print("\n contents of file "+str(i+1)+": "+str(content))