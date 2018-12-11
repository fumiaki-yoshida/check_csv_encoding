import os
import glob
import chardet

path = input('input a csv_file path:')
os.chdir(path)

csv_files = glob.glob('*.csv')
for csv_file in csv_files:
    f = open(csv_file, "rb").read()
    print(csv_file, chardet.detect(f))
