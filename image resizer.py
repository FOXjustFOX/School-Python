from PIL import Image
import os
b = 0
l= []
for i in range(11):
    l.append(str(i))



for im in os.listdir('animation/right'):
    path = 'animation/right/'+im
    image = Image.open(path)
    new_image = image.resize((40,100))
    name = 'West'+l[b]+'.png'
    new_image.save(name)
    #print(name)
    b+=1