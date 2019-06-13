import os, xlrd, xlwt, time
import testcase_excel
import os

# 通过传入用例名称的文件和excel页面来读取测试用例
def get_case(filename, sheetnum):
    case_dir = os.getcwd() + "\\"+filename + '.xlsx'
    print(case_dir)
    datas = xlrd.open_workbook(case_dir)
    table = datas.sheets()[sheetnum]
    rows = table.nrows
    cols = table.ncols
    return rows, table


# 通过xlwt库来设计测试报告并写入excel里面
def write_report():
    workbook = xlwt.Workbook(encoding='utf-8')
    # 在excel测试报告表格中创建名叫housemanage的页面
    worksheet = workbook.add_sheet('result')
    # 设置字体格式为居中对齐
    alignment = xlwt.Alignment()
    alignment.horz = alignment.HORZ_CENTER
    alignment.vert = alignment.VERT_CENTER
    style = xlwt.XFStyle()
    style.alignment = alignment

    worksheet.write(0, 0, '序号')
    worksheet.write(0, 1, '用例')
    worksheet.write(0, 2, 'appId')
    worksheet.write(0, 3, 'appVersion')
    worksheet.write(0, 4, 'clientId')
    worksheet.write(0, 5, 'sequenceId')
    worksheet.write(0, 6, 'accessToken')
    worksheet.write(0, 7, 'sign')
    worksheet.write(0, 8, 'timestamp')
    worksheet.write(0, 9, 'language')
    worksheet.write(0, 10, 'timezone')
    worksheet.write(0, 11, 'Content-Type')
    worksheet.write(0, 12, 'deviceid')
    worksheet.write(0, 13, '是否通过')
    worksheet.write(0, 14, '期望结果')
    worksheet.write(0, 15, '实际结果')

    # 最后返回worksheet,workbook两个参数，因为在测试测试用例和运行文件中需要用到的两个参数
    return worksheet, workbook
