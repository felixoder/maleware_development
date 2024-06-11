import os

files = []

for file in os.listdir():
	if file == "encrypt.py":
		continue
	if os.path.isfile(file):

		files.append(file)


print(files)



