import pandas as pd

path = 'C:\\Users\\syahi\\OneDrive - studentupmedumy.onmicrosoft.com\\Satellite Technology\\Assignments\\Semester project\\'
data=pd.read_pickle(str(path)+'hashmap.pkl')

def loadDF(data):
    return pd.read_pickle(data)

def requestLonLat(name,Lat,Lon):
    df=loadDF(str(path)+'hashmap.pkl')
    dist=0.3
    sub=df[df['Latitude']<=Lat+dist]
    sub=sub[sub['Latitude']>=Lat-dist]
    subsub=sub[sub['Longitude']<=Lon+dist]
    subsub=subsub[subsub['Longitude']>=Lon-dist]

    timelist=data.drop_duplicates(subset=['time'])
    liste.rec = formFileName(timelist)
    print('Number of Images of', name, ':', len(liste))
    print('Number of passes:', len(set(rec)),'>>',set(rec))

    saveAndzip(liste,name,Lat,Lon)
    print(liste.rec)

g=data[data['time']=='2020-08-29 01:42:31.570000+00:00']
g=g['SunAngle']
print(g)

'''
data.describe() #--> shows if data was loaded correctly
print(data.describe)

timelist=data.drop_duplicates(subset=['time']) #--> extracts all times
print('time')
print(timelist)

data.axes #--> lists all values that can be used for filtering, e.g.
"time", "pictureNumber",...


sub=data[data['pictureNumber']==3]    #--> filter your database for attributes

'''
