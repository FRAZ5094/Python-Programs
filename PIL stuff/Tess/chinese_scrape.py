import pytesseract as tess
tess.pytesseract.tesseract_cmd=r"C:\\Users\\frase\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
from PIL import Image
from time import perf_counter


start=perf_counter()
img=Image.open("Page-12223.png")
text=tess.image_to_string(img,lang="chi_sim")
img.close()
print(text)
end=perf_counter()
print(f"took {round(end-start,2)} seconds")


#,lang="chi_sim"