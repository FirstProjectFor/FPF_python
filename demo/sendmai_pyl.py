import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendMail:
    """
    发送邮件
    目前可以通过 Gmail 发送邮件
    """

    def __init__(self):
        self.SMTP = "smtp.gmail.com:587"

    def send_by_gmail(self, g_username, g_password, title, content, send_to):
        """
        使用Gmail发送邮件
        :param g_username: gmail用户名
        :param g_password: gmail密码
        :param title:     邮件标题
        :param content:   邮件内容
        :param send_to:   发送给谁[数组],such as ["sunfeilong1993@163.com"
        :return: void
        """
        # 邮件对象
        msg = MIMEMultipart('alternative')
        msg['Subject'] = title
        msg['From'] = g_username
        msg['To'] = ",".join(send_to)
        # 邮件数据
        msg_data = MIMEText(content, 'plain')
        msg.attach(msg_data)

        mail_server = smtplib.SMTP(self.SMTP)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(g_username, g_password)
        mail_server.sendmail(from_addr=g_username, to_addrs=send_to, msg=msg.as_string())
        mail_server.quit()


to = ["sunfeilong1993@163.com"]
username = "sunfeilong1993@gmail.com"

sendMail = SendMail()
sendMail.send_by_gmail(g_username=username, g_password="*", title="Test", content="Hello Man!", send_to=to)
