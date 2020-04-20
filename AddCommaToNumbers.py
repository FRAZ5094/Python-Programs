number=123456789123456789

numberlen=len(str(number))
numberComma=int((numberlen-1)/3)
numberstart=numberlen-3*numberComma

Comma=str(number)

for i in range(numberComma):
    Comma=Comma[0:numberstart+4*i]+","+ Comma[numberstart+4*i:]
    print("Comma {} insert: {}".format(i+1,Comma))


print(" ")
print(".format Method {:,d}".format(number))
print("Program Method {}".format(Comma))
