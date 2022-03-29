import openpyxl

# 생성시 기본적으로 sheet1이 생성된다.
wb= openpyxl.Workbook()
sheet= wb.active

# B행4열에 입력 . . . 다음응용
sheet['B2'] = '메인 데이터 입력'
sheet['C5'] = '여기는 C5'

# E행 3열
sheet.cell(row=3, column=5).value='3.3'

sheet.append([1, 2, 3, 4, 5])


# 액셀명 파일 저장 ?if문으로 파일명 체크할수 없을까? 할수 있을거 같은데 알고리즘 안떠오른다.
wb.save('pyxlmain.xlsx')

# ws= wb.active
# ws.title='openpyxl_main'



