# write into empty txt file
file = open('/ExceptionalHandlling\\demofile.txt', 'w')
file.write('This is first line...\n')
file.write('this is second line...\n')
file.close()

# read from the file

file = open('/ExceptionalHandlling\\demofile.txt', 'r')
print(file.read())  # reading full contents
# print(file.readline())      # reading first line
# print(file.readlines())     # reading full contents
# print(file.readable())        # return true or false

# append the contents
file = open('/ExceptionalHandlling\\demofile.txt', 'a')
file.write('This is third line....')