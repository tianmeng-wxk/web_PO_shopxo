import yaml,xlrd,openpyxl
import smtplib
from email.mime.text import MIMEText
#from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
from log.log import Logger
from selenium import webdriver
from options.chrome_options import Options

def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)  # 或者yaml.full_load()
        return yaml_data
#read_yaml("../config/login.yaml")

#发送邮件
class SendEmail:
    def send_email(self,email_path):
        message = MIMEMultipart()
        #邮件内容
        text = """
        请输入你想说的邮件内容
        """
        message.attach(MIMEText(_text=text, _subtype='plain', _charset="utf-8"))
        #需要发送的附件的路径
        with open(email_path, 'rb') as f:
            content = f.read()
        att1 = MIMEText(content, "base64", "utf-8")
        att1["Content-Type"] = 'application/octet-stream'
        att1['Content-Disposition'] = 'attachment; filename = "report.html"'
        message.attach(att1)

        #邮件主题
        message["Subject"] = Header("主题", "utf-8").encode()
        message["From"] = Header("tianmeng", "utf-8")
        message["To"] = Header('tianmeng_wxk', "utf-8")

        try:
            smtp = smtplib.SMTP()
            #smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
            smtp.connect(host="smtp.qq.com", port=587)
            smtp.login(user="3394788013@qq.com", password="lizceyidpekpdbhd")
            sender = "3394788013@qq.com"
            receiver = ['tianmeng_wxk@163.com']
            smtp.sendmail(sender, receiver, message.as_string())
            Logger().log().info("发送邮件成功")
            return email_path
        except smtplib.SMTPException as e:
            Logger().log().info("发送邮件失败，失败信息：{}".format(e))

#xlrd读取excel
class ReadExcel:
    def __init__(self, excel_path, sheet_name):
        self.workbook = xlrd.open_workbook(excel_path)
        self.worksheet = self.workbook.sheet_by_name(sheet_name)
        self.rownum = self.worksheet.nrows
        self.colnum = self.worksheet.ncols

    def dict_data(self):
        if self.rownum <= 1:
             print("表格行数小于等于1，不能进行自动化")
        else:
             list = []
             self.headers = self.worksheet.row_values(0)
             #self.headers = self.worksheet.row_values(0)
             #j = 1#从1开始
             for i in range(1, self.rownum):
                 s = {}
                 values = self.worksheet.row_values(i)

                 for x in range(self.colnum):
                    s[self.headers[x]] = values[x]
                 list.append(s)
                 #j += 1
             return list

#openpyxl读取excel
def load_data(excel_path,sheet_name):
    excel = openpyxl.load_workbook(excel_path)
    sheet = excel[sheet_name]
    rows = sheet.max_row
    cols = sheet.max_column
    list = []
    for i in range(2,rows+1):
        dict = {}
        for j in range(1,cols+1):
            cell = sheet.cell(i, j)
            key = sheet.cell(1, j).value
            dict[key] = cell.value
        list.append(dict)
    print(list)
    return list

#load_data(r'D:\PO_shopxo\config\search.xlsx','Sheet1')

#打开浏览器类型
def browser_type(type):
    type = type.upper()
    if type == "CHR":
        Logger().log().info('正常启动谷歌浏览器中......')
        driver = webdriver.Chrome(options=Options().options_conf())
    elif type == "IE":
        Logger().log().info('正常启动IE浏览器中......')
        driver = webdriver.Ie()
    elif type == "FF":
        Logger().log().info('正常启动火狐浏览器中......')
        driver = webdriver.Firefox()
    else:
        Logger().log().info('输入浏览器类型失败，默认启用chrome浏览器')
        driver = webdriver.Chrome()
    return driver