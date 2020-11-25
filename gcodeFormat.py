import sys, os


def generate_message():
    message = 'M117 {0}-{1}'.format(current_line, current_layer)
    if layer_count > 0:
        message = '{0} of {1}'.format(message, layer_count)
    if current_type != '':
        message = '{0} {1}'.format(message, current_type)
    return message + '\n'


source_file_name = sys.argv[1]

splitName = os.path.splitext(source_file_name)
newFileName = splitName[0] + '_m' + splitName[1]

with  open(source_file_name, 'r') as f:
    sourceContent = f.readlines()

print('Source file name: {0}'.format(source_file_name))
print('New file name: {0}'.format(newFileName))
print('Source file has {0} lines'.format(len(sourceContent)))

layer_count = -1
current_layer = -1
current_type = ''
current_line = 1
# write new file
with open(newFileName, 'w') as f:
    for line in sourceContent:
        f.write(line)
        current_line = current_line + 1
        if layer_count < 0 and line.startswith(';Layer count:'):
            layer_count = int(line[14:-1])
            print('layers count: {0}'.format(layer_count))
        if line.startswith(';LAYER:'):
            current_layer = line[7:-1]
            current_type = ''
            f.write(generate_message())
            current_line = current_line + 1
        if line.startswith(';TYPE:'):
            current_type = line[6:-1]
            f.write(generate_message())
            current_line = current_line + 1
print('New file has {0} lines'.format(current_line))
