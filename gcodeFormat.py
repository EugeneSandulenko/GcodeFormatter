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

layer_count = -1
# writ new file
with open(newFileName, 'w') as f:
    for line in sourceContent:
        f.write(line)
        if layer_count < 0 and line.startswith(';Layer count:'):
            layer_count = int(line[14:-1])
            print('layers count: ', layer_count)
        if line.startswith(';LAYER:'):
            if layer_count > 0:
                f.write('M117 {0} of {1}\n'.format(line[1:-1], layer_count))
            else:
                f.write('M117 {0}'.format(line[1:]))
