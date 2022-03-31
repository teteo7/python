def filecheck():
    import os

    filename = 'pyxlmain'  # 파일명 고정값
    file_ext = '.xlsx'  # 파일 형식
    # output_path = 'C:/Users/KK/PycharmProjects/python/work_helper/%s%s' %(filename, file_ext)
    # output_path = 'C:/Users/%s%s' %(filename, file_ext)
    output_path = 'C:/Program Files/py/python/%s%s' %(filename, file_ext)

    uniq = 1
    while os.path.exists(output_path):  # 입력된 경로에 동일한 파일명이 존재할 때
        # output_path = 'C:/Users/KK/PycharmProjects/python/work_helper/%s%d%s' % (filename, uniq, file_ext)  # 파일명(1) 파일명(2)...
        output_path = 'C:/Program Files/py/python/%s%d%s' % (filename, uniq, file_ext)  # 파일명(1) 파일명(2)...
        uniq += 1
        print(output_path)
        print("모듈파일:", type(output_path))
        print("==================")

