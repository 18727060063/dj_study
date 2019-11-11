import xlrd

#添加普通人员数据
from DjangoApp.models import NormalPeople

def readTecExcel():
    work_book = xlrd.open_workbook("source/normalpeople.xls")
    sheet = work_book.sheet_by_index(0)
    row_count = sheet.nrows  # 行数
    col_count = sheet.ncols  # 列数
    sql_str = "insert into DjangoApp_normalpeople "
    for i in range(1, row_count):
        model = NormalPeople()

        for j in range(0, col_count):
            model.pTel = sheet.row_values(i)[0]
            model.pDesc = sheet.row_values(i)[1]
            model.pHostName = sheet.row_values(i)[2]
            model.pAddress = sheet.row_values(i)[3]
            model.id = sheet.row_values(i)[4]
            model.pRelation = sheet.row_values(i)[5]
            model.pFamilyNo = sheet.row_values(i)[6]
            model.pSpecial = sheet.row_values(i)[7]
            model.pName = sheet.row_values(i)[8]
            model.pIdNo = sheet.row_values(i)[9]
            model.pGender = sheet.row_values(i)[10]
        sql = "UNION SELECT '%s','%s','%s',%d,'%s','%s','%s','%s','%s','%s',%d" % (model.pTel, model.pDesc, model.pHostName, model.pAddress, model.pRelation, model.pFamilyNo, model.pSpecial, model.pName, model.pIdNo, model.pGender,model.id)
        print(sql)
