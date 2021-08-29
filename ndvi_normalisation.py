import joblib
import cv2
import matplotlib.pyplot as plt
import numpy as np

path='C:\\Users\\syahi\\OneDrive - studentupmedumy.onmicrosoft.com\\Satellite Technology\\Assignments\\Semester project\\'   #path to .joblib file
path+='NDVI_database_2020.joblib'

k=joblib.load(path, mmap_mode=None)

image_name='2020-08-29T01-42-31.570Z'

for i in k:     # list all images in database
    if i[0]==image_name:
        ndviImg = i[1]
        file_name = i[0]

mini = np.nanmin(ndviImg)
maxi = np.nanmax(ndviImg)

print(mini,maxi)

cmap = plt.cm.rainbow
norm = plt.Normalize(vmin=mini, vmax=maxi)
image = cmap(norm(ndviImg))

cv2.imshow(file_name,image)
