import joblib

path='C:\\Users\\Boettcher\\Nextcloud\\9004_Malaysia_Borneo\\POI_export\\Group02\\' #--> replace that with your path!

path+='NDVI_database.joblib'

k=joblib.load(path, mmap_mode=None)
##### Structure ########################################
#####################
#####  Image Name = '2019-03-10T03-10-53.546Z'
#####  NDVI[y,x] = NDVI_value
#
#   [ [Image Name, [NDVI[y,x]] ], ....]
#########################################################

print (len(k)) # --> Number of Images

print (k[0][0]) # --> File Name of first Image in Database
print (k[2][0]) # --> File Name of 2nd Image in Database

for i in k:     # --> list all Images names in database
    print (i[0])

print (k[0][1][150,150]) # --> NDVI Value of first Image of Pixel [150,150]
