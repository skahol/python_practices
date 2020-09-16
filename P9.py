import os
def print_tree(path):
    if os.path.isdir(path) == True:
        for dirpath, dirs, files in os.walk(path):
            d_path = dirpath.split('/')
            print('|', (len(path))*'---', '[',os.path.basename(dirpath),']')
               
            for f in files:
                print('|', len(d_path)*'---',f)
                #print(os.path.join(path,f))

print_tree('C:\\Users\\Asus\\calculator')