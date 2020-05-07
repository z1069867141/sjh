import pymysql
import time

class mysql_function(object):
    def __init__(self):
        self.connect = pymysql.Connect(
            host='139.196.183.76',
            port=3306,
            user='test201906',
            passwd='qytest201906',
            db='b2bsaas',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()
        self.time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    # 搜索手机登录验证码
    def search_sms_log(self,phone):
        time.sleep(2)
        sql_search = 'SELECT code FROM `qy_sms_log` where mobile = {phone} and create_time >= "{time}"order by create_time desc limit 1'.format(phone=phone,time=self.time)
        # print(sql_search)
        self.cursor.execute(sql_search)
        row_3 = self.cursor.fetchall()
        row_4 = row_3[0][0]
        self.cursor.close()
        self.connect.close()
        return row_4

if __name__ == "__main__":
    search = mysql_function()
    search.search_sms_log("15011111111")