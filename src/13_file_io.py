"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

file = open('src/foo.txt')
print(file.read())
file.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

file2 = open('src/bar.txt','w')
file2.write('In the twilight rain ')
file2.write('these brilliant-hued hibiscus - ')
file2.write('A lovely sunset.')
file2.close()


file3 = open('src/bar.txt')
print(file3.read())
file3.close()
