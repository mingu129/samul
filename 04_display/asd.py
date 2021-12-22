import os

dir_path = str(os.path.dirname(os.path.realpath(__file__)))

path = dir_path + '/static'

files = os.listdir(path)

for f in files:
    print(f)
