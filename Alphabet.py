Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n=27
while n>26 or n<0:
    n=int(input("Enter the number of Alphabet to print"))
    if n>26:
        print("No Taylor there are only 26 numbers in the alphabet, choose another")
    if n<0:
        print("number must be positive, choose another")
nAlphabet=""
for i in range(n):
    nAlphabet+=Alphabet[i]
print("These are the first {} letters in the Alphabet:".format(n))
print(nAlphabet)
