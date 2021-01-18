
file_name=__file__[::-1]

i=file_name.index("/")

file_name=file_name[i::][::-1]

print(file_name)