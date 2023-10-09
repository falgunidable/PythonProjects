import os

#   r = read
#   a = append
#   w = write
#   x = create

#   Read - error raised if file doesn't exist t - text file b - binary file

f = open("./text_files/names.txt",'r')     # if we don't specify r than it is still r(read) by default
# print(f.read())
# print(f.read(4))        # reads only first 4 characters from the file
print(f.readline())       # reads the entire line of the file till the end
print(f.readline())

for line in f:
    print(line)     # reads line by line till the end

f.close()   # always try to close the open file, if changes are made then should not be reflected

try:
    f = open("./text_files/more_names.txt")
    print(f.read())
except:
    print("No file found")
finally:
    f.close()

# append - creates the file if it doesn't exist
f = open("./text_files/more_names.txt",'a')
f.write("\nNeil")
f.close()

f = open("./text_files/more_names.txt")
print(f.read())
f.close()

f = open("./text_files/names_list.txt",'a')     # new file created
f.write("Neil\nSiatara\nForever")
f.close()

f = open("./text_files/names_list.txt")
print(f.read())
f.close()

# write - (overwrite the existing file)
f = open("./text_files/names_list.txt",'w')     # new file can also be created using w
f.write('NEW STUDENT NAMES TO BE WRITTEN')
f.close()

f = open("./text_files/names_list.txt")
print(f.read())
f.close()

# two ways to create a new file

# opens a file for writing, creates the file if it doesn't exist

# creates the specified file, but returns an error if the file exists

if not os.path.exists("dave.txt"):      # need to import os for path check
    f = open("./text_files/dave.txt","x")
    f.close()

# delete a file

# avoid an error if it doesn't exist

if os.path.exists("./text_files/dave.txt"):
    os.remove("./text_files/dave.txt")
else:
    print("the file to delete doesn't exist")

with open('./text_files/more_names.txt') as f:
    context = f.read()

with open('./text_files/names.txt','w') as f:
    f.write(context)