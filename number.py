# 本项目来自Feipi的意见，由ChinePyStudio和Feipi共同创作
# 本项目在GitHub开源，可在CSDN下载也可在GitHub下载
# 如果有对本项目有意见的，可以联系feipinet@163.com或chinepy@qun.mail.163.com以及在GitHub里提出意见

# 前置操作
import datetime  # 年龄判断使用
import json  # 读取JSON用

class NumBerUse:
    def __init__(self, num, admin = False):
        self.if_admin = admin
        self.out_logs("身份证测验系统，版本1.0.7 | 本软件仅支持中国身份证")
        self.num = num
        self.checknum()
        if admin:
            self.start_admain()
        else:
            self.out_logs("未开启管理员模式，某些功能可能无法操作！", 1)

    # 启动管理员模式
    def start_admain(self):
        f = open("administrators.cfg","w+",encoding="utf8")
        if f.read() == "":
            self.out_logs("发现内容缺失，启用输入模式 | 请在日志区域输入")
            username = self.out_logs("输入用户名", -1)
            password = self.out_logs("请输入密码", -1)
            admin = {"username" : username,"password" : password}
            json_data = json.dumps(admin)
            f.write(json_data)
            self.out_logs("已载入内容")
        else:
            things = f.read()
            json_data = json.loads(things)
            self.out_logs("已检测到配置文件，开始验证...")
            username = self.out_logs("请输入用户名", -1)
            password = self.out_logs("请输入密码", -1)
            if json_data["username"] == username and json_data["password"] == password:
                self.if_admain = True
                self.out_logs("验证完成！")
                return
            else:
                self.out_logs("用户名或密码错误", 2)


# 日志输出函数
    def out_logs(self, things, mode = 0):
        if mode == 0:
            print("[身份证插件·日志/INFO]->" + things)
        elif mode == 1:
            print("[警告/Warning] >:" + things)
        elif mode == 2:
            print("[错误/Error] >>" + things)
        elif mode == -1:
            print("[日志输入系统/Input] >>" + things)
            In = input()
            return In

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
                self.out_logs("验证成功")
                return True
            except:
                # 校验码是否为X
                if self.num[17] == "X":
                    return True
                else:
                    self.out_logs("验证失败，格式错误", -1)
                    return False
            finally:
                # 释放内存
                pass

    # 存储用户数据
    def save_cfg(self):
        self.out_logs("该操作可能导致信息泄露，请全面杀毒并确保服务端安全后在使用保存功能", 1)
        f = open("save.json", "a+", encoding="utf8")
        if self.if_admin:
            num = self.num
            sex = self.sex()
            age = self.showage()
            user = {"Num" : num,"Sex" : sex, "Age" : age}
            json_data = json.dumps(user)
            self.out_logs("存储成功！")
            return
        else:
            self.out_logs("未获得管理员权限！", -1)

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
