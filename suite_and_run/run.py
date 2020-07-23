import pytest
#pytest.main(["-s","-vv","../../testingshop","--html=../config/report/pytest_report.html"])
#"--maxfail=1","-n=2"

#生成allure测试报告
# pytest.main(['-s','-q','./test_cases.py','--alluredir','../config/report/xml'])
#命令行
#allure generate --clean ../config/report/xml/ -o ../config/report/allure_html


#生成allure方法二
if __name__ == '__main__':
    import os
    pytest.main(['-s','-q','../test_case/test_cases.py','--alluredir=../report/allure_xml'])#生成alure缓存文件
    os.system('allure generate --clean ../report/allure_xml/ -o ../report/allure_html')
    #os.system('allure serve ./report/xml')