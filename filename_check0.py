import os


def fcheck():
    filename = 'pyxlmain'  # 파일명 고정값
    file_ext = '.xlsx'  # 파일 형식
    output_path = 'C:/Users/KK/PycharmProjects/python/%s%s' %(filename, file_ext)
    uniq = 1
    while os.path.exists(output_path):  # 동일한 파일명이 존재할 때
        output_path = 'C:/Users/KK/PycharmProjects/python/%s%d%s' %(filename, uniq, file_ext)  # 파일명(1) 파일명(2)...
        uniq += 1
        print(type(output_path))
    return output_path