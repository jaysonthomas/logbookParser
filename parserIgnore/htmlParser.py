import os
import os.path as path

def absoluteFilePaths(directory):
  for dirpath,_,filenames in os.walk(directory):
    print(dirpath)
    for f in filenames:
      yield os.path.abspath(os.path.join(dirpath, f))

def list_files(startpath):
  for root, dirs, files in os.walk(startpath):
    if ('.git' in root):
      continue
    elif (root == startpath):
      levelFromStart = 0
    else:
      levelFromStart = root.replace(startpath, '').count(path.sep) + 1
    
    print(f'{os.path.basename(root)}/')
    subindent = '../' * (levelFromStart)
    for f in files:
        print(f"{subindent}{f}  {root+path.sep+f}")


# test = absoluteFilePaths('/home/jayson/P/test/')
# for i in test:
#   print(i)

list_files('/home/jayson/P/logbookParser/')

# exclude = ['.cache']
# def find(name, path):
#   for root, dirs, files in os.walk(path, topdown=True):
#     # if name in files:
#       # print(f'Directory: {dirs}')
#       return os.path.join(root, name)

# print(find('index.html', '/home/jayson/logbook/'))

# from pathlib import Path
# print(Path('dir1/h1.html').absolute())
# print(os.path.realpath('dir1/h1.html'))
# if __name__ == "__main__":
#   for (root,dirs,files) in os.walk('~/logbook/', topdown=True):
#       print (f'Root: {root}')
#       print (f'Dirs: {dirs}')
#       print (f'files: {files}')
#       print ('--------------------------------')

#       break