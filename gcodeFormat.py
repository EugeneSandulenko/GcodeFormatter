# Python code to 
# demonstrate readlines() 

import sys, os

source_file_name = sys.argv[1]

splitName = os.path.splitext(source_file_name)
newFileName = splitName[0] + '_m' + splitName[1]

print('Source file name: {0}'.format(source_file_name))
print('New file name: {0}'.format(newFileName))

sourceFile = open(source_file_name, 'r')
sourceContent = sourceFile.readlines()
sourceFile.close()

print('Source file has {0} lines'.format(len(sourceContent)))

layer_count = -1
current_layer = -1
current_type = ''
current_layer_message = ''
# write new file
with open(newFileName, 'w') as f:
    for line in sourceContent:
        f.write(line)
        if layer_count < 0 and line.startswith(';Layer count:'):
            layer_count = int(line[14:-1])
            print('layers count: {0}'.format(layer_count))
        if line.startswith(';LAYER:'):
            current_layer = line[1:-1]
            current_type = ''
            current_layer_message = 'M117 {0}\n'.format(current_layer)
            if layer_count > 0:
                current_layer_message = 'M117 {0} of {1}\n'.format(current_layer, layer_count, current_type)
            f.write(current_layer_message)
        if line.startswith(';TYPE:'):
            current_type = line[6:]
            f.write('{0} {1}'.format(current_layer_message[:-1], current_type))
