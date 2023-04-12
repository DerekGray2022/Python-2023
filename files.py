# Python has functions for creating, reading, updating, and deleting files.

''' Create File '''
newFile = open("testFile.txt", "w")


''' Get some info   '''
print(f"Name: {newFile.name}")
# print(f"Is_Closed: {newFile.closed}")
# print(f"Opening Mode: {newFile.mode}")


''' Write to file   '''
newFile.write("This is a Python page ")
newFile.write("and I like Javascript")
newFile.close()


''' Append file  '''
newFile = open("testFile.txt", "a")
newFile.write(", I also like ReactJs.")
newFile.close()


''' Read from file  '''
newFile = open("testFile.txt", "r+")
text = newFile.read(100)
print(text)
newFile.close()

newFile = open("testFile.txt", "r+")




