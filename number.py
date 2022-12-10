# 本项目来自Feipi的意见，由ChinePyStudio和Feipi共同创作
# 本项目在GitHub开源，可在CSDN下载也可在GitHub下载
# 如果有对本项目有意见的，可以联系feipinet@163.com或chinepy@qun.mail.163.com以及在GitHub里提出意见

# 前置操作
import datetime  # 年龄判断使用
import json  # 读取JSON用

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
                # 校验码是否为X
                if self.num[17] == "X":
                    return True
                else:
                    print("错误")
                    return False
            finally:
                # 释放内存
                print("完毕")
    # 查看年龄
    def showage(self):
        today = datetime.date.today()  # 今天的日期
        year = today.year  # 今年的年份
        num_year = int(self.num[6:10])  # 截取到身份证中的日期
        age = year - num_year  # 得出年龄
        return age  # 返回年龄

    # 查看性别
    def sex(self):
        sex_num = self.num[16]
        # 判断男女
        if int(sex_num) % 2 == 0:
            return "女"
        elif int(sex_num) % 2 == 1:
            return "男"

    # 检测地区（城市、省份）
    def city_load(self):
        f = open("city.json","r",encoding="utf8")
        json_text = f.read()
        city = json.loads(json_text)
        city_num = self.num[:2]
        City_china = city[city_num]
        return City_china;
