# 本文档作为测试问道使用，为保证数据的正确！

import number

# 输入身份证号
num = input("请输入身份证号：\n")
# 创建对象
test = number.NumBerUse(num)
# 性别
sex_num = test.sex()
print("您的年龄为：{0}".format(sex_num))
# 年龄
age = test.showage()
print("您的年龄为：{0}".format(age))
# 检测城市（地区、区域）
city = test.city_load()
print("您在的地区：{0}".format(city))
