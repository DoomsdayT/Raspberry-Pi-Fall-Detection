import sys
sys.path.append("../")
import schedule
import time
from detection.detect import detect
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def emailTask ():
    sender = 'from@runoob.com'
    receivers = ['270001151@qq.com']

    message = MIMEText('跌倒', 'plain', 'utf-8')
    message['From'] = Header("跌倒人", 'utf-8')
    message['To'] =  Header("接收人", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    print('message')
    try:
        smtpObj = smtplib.SMTP('localhost', 25)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
def detectTask ():
    isFall = detect([9.0, 9.8, 10.0, 6.0])
    if isFall > 0.2:
        print('fall')
        # emailTask()

if __name__ == '__main__':
    # emailTask()
    schedule.every(10).seconds.do(detectTask)
    while True:
        schedule.run_pending()
        time.sleep(1)
