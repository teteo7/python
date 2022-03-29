import os
import re
#파일명만 받고싶으면 [0]
filename= os.path.splitext('pyxlmain.xlsx')[0]
print(filename)

#확장자만 받고싶으면[1]
# filename= os.path.splitext('pyxlmain.xlsx')[1]
# print(filename)
# print("======================")

#문자열 공백 제거후 if문으로 파일 체크
for a in range(1, 5):
    print(filename, a, '.xlsx')

    b= filename, a, '.xlsx'
    print(b)

