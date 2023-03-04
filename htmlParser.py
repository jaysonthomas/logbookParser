import os

def absoluteFilePaths(directory):
  for dirpath,_,filenames in os.walk(directory):
    print(dirpath)
    for f in filenames:
      yield os.path.abspath(os.path.join(dirpath, f))

def list_files(startpath):
  for root, dirs, files in os.walk(startpath):
    level = root.replace(startpath, '').count(os.sep)
    print(f'level:{level}')
    indent = ' ' * 4 * (level)
    print('{}{}/'.format(indent, os.path.basename(root)))
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print('{}{}'.format(subindent, f))

test = absoluteFilePaths('/home/jayson/P/test/')
for i in test:
  print(i)

list_files('/home/jayson/P/test/')

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