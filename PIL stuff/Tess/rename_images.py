import pytesseract as tess
tess.pytesseract.tesseract_cmd=r"C:\\Users\\frase\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
from PIL import Image
from time import perf_counter
import glob
import os 

files=glob.glob("./*.png")

start=perf_counter()
for file in files:
    img=Image.open(file)
    cropped=img.crop((380,img.height-70,img.width-350,img.height-40))
    text=tess.image_to_string(cropped)
    img.close()
    index=text.find("/")
    name=f"Page-{text[:index]}.png"
    os.rename(file,name)
    print(f"{file[2:]}=>{name}")

end=perf_counter()
print(f"took {round(end-start,2)} seconds")


#,lang="chi_sim"