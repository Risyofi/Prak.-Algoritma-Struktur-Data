staff = {'Santi'   : 'santi@ums.ac.id', \
         'Jokowi'  : 'jokowi@solokab.go.id', \
         'Endang'  : 'Endang@yahoo.com', \
         'Sulastri': 'Sulastri3@gmail.com'}

yangDicari = 'Santi'
if yangDicari in staff:
    print('emailnya', yangDicari, 'adalah', staff[yangDicari])
else:
    print('tidak ada yang namanya', yangDicari)