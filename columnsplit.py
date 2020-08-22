import numpy as np
image_urls =np.array([
    "001.jpeg",
    "002.jpeg",
    "003.jpeg",
    "004.jpeg",
    "005.jpeg",
    "006.jpeg",
    "007.jpeg",
    "008.jpeg",
    "009.jpeg",
    "010.jpeg",
    "011.jpeg",
    "012.jpeg",
    "013.jpeg",
    "014.jpeg",
    "015.jpeg",
    "016.jpeg",
    "017.jpeg",
    "018.jpeg",
    "019.jpeg",
    "020.jpeg",
    "021.jpeg",
    "022.jpeg",
    "023.jpeg",
    "024.jpeg",
    "025.jpeg",
    "026.jpeg",
    "027.jpeg",
    "028.jpeg",
    "029.jpeg",
    "030.jpeg",
    "031.jpeg",
    "032.jpeg",
    "033.jpeg",
    "034.jpeg",
    "035.jpeg",
    "036.jpeg",
    "037.jpeg",
    "038.jpeg"
])

scorePerPicture = 5
score = 500
n_cols = 3
image_urls = image_urls[:int(score/scorePerPicture)]

col1 = []
col2 = []
col3 = []
col4 = []

for i, image_url in enumerate(image_urls):
    if i % 4 == 0:
        col1.append(image_url)
    elif i % 4 == 1:
        col2.append(image_url)
    elif i % 4 == 2:
        col3.append(image_url)
    else:
        col4.append(image_url)

image_urls = [col1, col2, col3,col4]

#print(image_urls)

for row in image_urls:
    for url in row:
        print(url)