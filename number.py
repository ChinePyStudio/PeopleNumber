# 本项目来自Feipi的意见，由ChinePyStudio和Feipi共同创作
# 本项目在GitHub开源，可在CSDN下载也可在GitHub下载
# 如果有对本项目有意见的，可以联系feipinet@163.com或chinepy@qun.mail.163.com以及在GitHub里提出意见

# 前置操作
import datetime  # 年龄判断使用

class NumBerUse:
    def __init__(self, num):
        print("身份证测验系统，版本1.0.7 | 本软件仅支持中国身份证")
        self.num = num
        self.checknum()

    # 检查身份证
    def checknum(self):
        # 判断身份证位数
        if len(self.num) != 18:
            print("身份证位数错误！")
            return False
        elif len(self.num) == 18:
            try:
                # 判断是否为数字
                int(self.num)
                print("正确！")
                return True
            except:
                print("错误")
                return False
            finally:
                # 释放内存
                print("完毕")
    # 查看年龄
    def showage(self):
        today = datetime.date.today()  # 今天的日期
        year = today.year  # 今年的年份
        num_year = self.num[6:14]  # 截取到身份证中的日期
        age = year - num_year  # 得出年龄
        return age  # 返回年龄