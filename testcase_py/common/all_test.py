from xlwt import XFStyle

from testcase_py.common.Readconfig import get_API_url
from testcase_py.common.ReadExcel import get_case, write_report,module_path
import requests, unittest, json
import os, xlrd, xlwt, time
import datetime
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../.."))+"\\config")
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../.."))+"\\report")
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../.."))+"\\testcase_excel")
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../.."))+"\\testcase_py")
print(sys.path)
def test_API():

    print("begin......")
    passed=0
    failed=0

    #设置重连次数

    #API_url ="http://221.122.92.15:11000/ai-access/nlp?engine=MusicBox&needcontent=yes"
    API_url=get_API_url("API_url")
    print(API_url)
    (rows, table) = get_case("testcase", 0)
    print(rows)
    (worksheet,workbook)=write_report()
    style=XFStyle()
    font = xlwt.Font()
    font.colour_index=2
    font.bold=True
    style.font=font

    # 获取excel表格里面需要给接口传入的参数
    for i in range(rows-1):
        appId = table.cell_value(i+1, 2)
        appVersion = table.cell_value(i+1, 3)
        clientId = table.cell_value(i+1, 4)
        sequenceId = table.cell_value(i+1, 5)
        accessToken = table.cell_value(i+1, 6)
        sign = table.cell_value(i+1, 7)
        timesample=table.cell_value(i+1,8)
        language=table.cell_value(i+1,9)
        timezone=table.cell_value(i+1,10)
        content_type = table.cell_value(i+1, 11)
        deviceid = table.cell_value(i+1, 12)
        query_content=table.cell_value(i+1,1)
        xunhao=table.cell_value(i+1,0)

        worksheet.write(i+1, 0, xunhao)
        worksheet.write(i+1, 1, query_content)
        worksheet.write(i+1, 2, appId)
        worksheet.write(i+1, 3, appVersion)
        worksheet.write(i+1, 4, clientId)
        worksheet.write(i+1, 5, sequenceId)
        worksheet.write(i+1, 6, accessToken)
        worksheet.write(i+1, 7, sign)
        worksheet.write(i+1, 8, timesample)
        worksheet.write(i+1, 9, language)
        worksheet.write(i+1, 10, timezone)
        worksheet.write(i+1, 11, content_type)
        worksheet.write(i+1, 12, deviceid)

        # 接口body需要传入的参数
        bodydata={"LIBaseinfo":{"query":query_content,"contextid":""},"opmode":"remote"}

        # 请求头，网站加了登陆验证之后需要在请求头传入Authorization参数
        headers = {"appId": appId,
                "appVersion": appVersion,
                "clientId": clientId,
                "sequenceId": sequenceId,
                "accessToken": accessToken,
                "sign": sign,
                "timestamp": timesample,
                "language": language,
                "timezone": timezone,
                "Content-Type": content_type,
                "deviceid": deviceid,
            }
        bodydata = json.dumps(bodydata)
        print(bodydata)
        print(headers)
        r = requests.post(API_url, data=bodydata, headers=headers)
        print("request end!")
        print (r.text)
        worksheet.write(i+1, 15, r.text)
        # 将字符串格式转换为字典
        b = eval(r.text)
        m = b.get('retCode')


        # 判断接口测试通过与否
        if m == "00000":
            worksheet.write(i+1, 13, '通过')
            passed += 1
            print(passed)
        else:
            worksheet.write(i+1, 13, '失败',style)
            failed += 1
            print(failed)
        print(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        workbook.save(module_path+'\\report\\'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'_result.xls')
        # 测试用例执行完后，返回用例成功与失败的数量

    return passed, failed

if __name__ == '__main__':
    print ("main")
    test_API()
