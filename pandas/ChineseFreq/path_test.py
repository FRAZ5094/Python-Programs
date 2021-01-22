path=__file__[::-1]

i=0
try:
    i=path.index("/")
except:
    pass
path=path[i::]
path=path[::-1]
if i==0:

    filename = "weibo_wordfreq.release_UTF-8.txt"
else:
    filename = f"{path}weibo_wordfreq.release_UTF-8.txt"

print(filename)