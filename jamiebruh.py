chars=[0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

combinations=[]

for digit1 in chars:
    for digit2 in chars:
        for digit3 in chars:
            combinations.append("{}{}{}".format(digit1,digit2,digit3))


already_made=["000","001","002"]

found=False

for combination in combinations:
    if combination not in already_made:
        email="{}@gmail.com".format(combination)
        already_made.append(combination)
        break

print(email)

