# Program #1: Item Counter
# Josiah Hendley
# 3/26/26
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    count = 0
    file = open("names.txt", "r")

    for line in file:
        count += 1

    file.close()
    print(count)

  



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
