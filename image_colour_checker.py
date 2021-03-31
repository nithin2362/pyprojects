from PIL import Image                           // Importing necessary modules
import numpy as np 



def is_color_image(image_name):                 // Returns whether an image is Colour or Black and White image

  image = Image.open(image_name)
  final = {True:'Colour Image',False:'Black and White Image'}
  arr = np.array(image)
  flag = False
  try:
    pxlen = len(arr[0][0])
  except:
    return flag

  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if list(arr[i][j]) != [arr[i][j][0]] * 3:
        flag = True
        break
  return final[flag]



print(is_color_image(input('Enter image name: '))) // Giving the full file path of the image is preferred.
