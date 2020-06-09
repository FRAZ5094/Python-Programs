import pyperclip
bruhlist=[]
bruhlist.append((1,2))
bruhlist.append((1,3))
pyperclip.copy(str(bruhlist))
spam = pyperclip.paste()

if (1,5) in bruhlist:
    print("True")
else:
    print("False")