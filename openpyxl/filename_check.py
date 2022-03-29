import os
import csv

input_path = r'D:/practice/original/'
filename = 'sample_merge'  # 파일명 고정값
file_ext = '.csv'  # 파일 형식

output_path = 'D:/practice/%s%s' % (filename, file_ext)
uniq = 1
while os.path.exists(output_path):  # 동일한 파일명이 존재할 때
    output_path = 'D:/practice/%s(%d)%s' % (filename, uniq, file_ext)  # 파일명(1) 파일명(2)...
    uniq += 1