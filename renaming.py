import os 

os.chdir('/Users/nielspace/Desktop/test')

for i in os.listdir():
    if i == '.DS_Store':
        continue
    filename, ext = (os.path.splitext(i))
    # print(filename.split(' '))
    title, copy, number = filename.split(' ')
    number = number.zfill(2)
    new = ('{}-{}{}'.format(number,title,ext))
    os.rename(i, new)
