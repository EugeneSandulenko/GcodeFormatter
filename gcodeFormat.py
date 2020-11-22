# Python code to 
# demonstrate readlines() 

import sys, os

sourceFileName = sys.argv[1];

splitName=os.path.splitext(sourceFileName)
newFileName = splitName[0] + '_m' + splitName[1];

print 'Source file name: ', sourceFileName
print 'New file name: ', newFileName

sourceFile = open(sourceFileName, 'r')
sourceContent = sourceFile.readlines()
sourceFile.close()

print 'Source file has  ', len(sourceContent), ' lines'

# writing to file
newFile = open(newFileName, 'w')
newFile.writelines(sourceContent)
newFile.close()
