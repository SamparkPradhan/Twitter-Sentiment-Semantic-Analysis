# importing os and re package
import re
import os

# Creating a string to add all contents of both sgm file
myList = ''

with open("reut2-020.sgm", "r") as sgmFile1:

    for line in sgmFile1:
        myList = myList+line

with open("reut2-021.sgm","r") as sgmFile2:

    for line1 in sgmFile2:
        myList = myList + line1

# Creating a list to get all contents between tag into each element
text = []
text = re.findall("<TEXT(.*?)</TEXT>", myList, re.S)

# Creating multiple files with each elements in list
countFiles = 1
for i in text:
    with open(os.path.join('sgmfiles',"%s_split_file.txt" % countFiles), "w") as f:
        f.write(i)
        countFiles = countFiles + 1
