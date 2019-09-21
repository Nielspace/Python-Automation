import os 

os.chdir('/Users/nielspace/Desktop/test')

for i in os.listdir():
    a,b = (os.path.splitext(i))
    print(a.split(' '))
