import smtplib
from _datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from apscheduler.schedulers.blocking import BlockingScheduler


class HeartbeatCheck:
    def __init__(self):
        self.SMTP = "smtp.gmail.com:587"
        self.out = open(file="log.txt", mode="a", encoding="utf-8")

    def __send_by_gmail(self, g_username, g_password, title, content, send_to):
        # 邮件对象
        msg = MIMEMultipart('alternative')
        msg['Subject'] = title
        msg['From'] = g_username
        msg['To'] = ",".join(send_to)
        # 邮件数据
        msg_data = MIMEText(content, 'plain')
        msg.attach(msg_data)

        mail_server = smtplib.SMTP(self.SMTP)
        try:
            mail_server.ehlo()
            mail_server.starttls()
            mail_server.ehlo()
            mail_server.login(g_username, g_password)
            mail_server.sendmail(from_addr=g_username, to_addrs=send_to, msg=msg.as_string())
            mail_server.quit()
            mail_server.close()
        except Exception as e:
            print("发送邮件出现异常: ", e, file=self.out)

    def __send_mail(self, title, content):
        self.__send_by_gmail(g_username="sunfeilong1993@gmail.com",
                             g_password="*",
                             title=title,
                             content=content,
                             send_to=["sunfeilong1993@163.com"])

    def send_self_heartbeat(self):
        self.__send_mail(title="心跳检测程序状态报告", content="心跳检测程序正在运行...")
        print("心跳检测程序发送状态报告...", file=self.out)
        self.out.flush()
        pass

    def check_heartbeat(self):
        # 检查服务器状态
        host = "http://www.sunfeilong.cn"
        res = requests.request("GET", host)
        if res.status_code != 200:
            msg = [
                "心跳检测程序没有检测到服务器没有回应",
                "响应码：" + res.status_code,
                "服务器：" + host,
                "日期：" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ]
            self.__send_mail(title="服务器异常", content="\r\n".join(msg))
            print("心跳检测程序没有检测到服务器没有回应... " + "\r\n".join(msg), file=self.out)
        else:
            print("server: " + host + " is running! ", file=self.out)
            self.out.flush()
            pass


if __name__ == '__main__':
    heartbeat = HeartbeatCheck()
    scheduler = BlockingScheduler()
    # 每天八点执行一次，发送邮件确定程序正常运行
    scheduler.add_job(heartbeat.send_self_heartbeat, "cron", day_of_week="0-6", hour=8, minute=0)
    # 每个三秒检查一次服务器是否正常
    scheduler.add_job(heartbeat.check_heartbeat, "interval", seconds=6)
    scheduler.start()
