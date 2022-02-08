'''

fh = open('pj.txt', 'w')
fh.write('hack the world')
fh.close()

'''

'''

fh = open('pj.txt', 'a')
content=fh.write('my dear pj')
print(content)
fh.close()

'''
#a for append, w for write and r for read and writelines also.


fh = open('pj.txt', 'r')
content=fh.readlines(1)
print(content)
fh.close()



