# Python code to 
# demonstrate readlines() 

import sys, os

source_file_name = sys.argv[1]

splitName = os.path.splitext(source_file_name)
newFileName = splitName[0] + '_m' + splitName[1]

print('Source file name: ', source_file_name)
print('New file name: ', newFileName)

sourceFile = open(source_file_name, 'r')
sourceContent = sourceFile.readlines()
sourceFile.close()

print('Source file has  ', len(sourceContent), ' lines')

# writ new file
with open(newFileName, 'w') as f:
    for line in sourceContent:
        f.write(line)
        if line.startswith(';LAYER:'):
            f.write('M117 %s' % line[1:])
